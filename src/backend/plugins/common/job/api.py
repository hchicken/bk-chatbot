"""
TencentBlueKing is pleased to support the open source community by making
蓝鲸智云PaaS平台社区版 (BlueKing PaaSCommunity Edition) available.
Copyright (C) 2017-2018 THL A29 Limited,
a Tencent company. All rights reserved.
Licensed under the MIT License (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
either express or implied. See the License for the
specific language governing permissions and limitations under the License.
"""

import json
import time
from typing import Union, List, Dict

from opsbot import CommandSession
from opsbot.exceptions import ActionFailed, HttpFailed
from opsbot.log import logger
from opsbot.plugins import GenericTask
from component import JOB, RedisClient, BK_JOB_DOMAIN, OrmClient


class JobTask(GenericTask):
    def __init__(self, session: CommandSession, bk_biz_id: Union[str, int] = None):
        super().__init__(session, bk_biz_id, RedisClient(env='prod'))
        self._job = JOB()

    async def _get_job_plan_list(self, **params) -> List:
        data = await self._job.get_job_plan_list(**params)
        bk_job_plans = data.get('data', [])
        bk_job_plans.sort(key=lambda x: x['last_modify_time'], reverse=True)
        return [{'id': str(job_plan['id']), 'text': job_plan['name'], 'is_checked': False}
                for job_plan in bk_job_plans[:20]]

    async def _get_job_plan_detail(self, **params) -> Dict:
        data = await self._job.get_job_plan_detail(**params)
        return data

    async def render_job_plan_list(self, **params):
        if not self.biz_id:
            return None

        bk_job_plans = await self._get_job_plan_list(bk_username=self.user_id, bk_biz_id=self.biz_id,
                                                     length=100, **params)
        template_card = {
            'card_type': 'vote_interaction',
            'source': {
                'desc': 'JOB',
                'desc_color': 1
            },
            'main_title': {
                'title': '欢迎使用JOB平台',
                'desc': '请选择JOB执行方案'
            },
            'task_id': str(int(time.time() * 100000)),
            'checkbox': {
                'question_key': 'bk_job_plan_id',
                'option_list': bk_job_plans
            },
            'submit_button': {
                'text': '确认',
                'key': 'bk_job_plan_select'
            }
        }
        return template_card

    async def render_job_plan_detail(self):
        if self._session.is_first_run:
            try:
                job_plan_id = self._session.ctx['SelectedItems']['SelectedItem']['OptionIds']['OptionId']
            except KeyError:
                return None

            bk_job_plan_detail = await self._get_job_plan_detail(bk_username=self.user_id, bk_biz_id=self.biz_id,
                                                                 job_plan_id=int(job_plan_id))
            global_var_list = [{'keyname': var['name'], 'value': var['value'] if var['value'] else '待输入'}
                               for var in bk_job_plan_detail.get('global_var_list', []) if var['type'] == 1]
            job_plan_name = bk_job_plan_detail["name"]
        else:
            job_plan_id = self._session.state['job_plan_id']
            job_plan_name = self._session.state['job_plan_name']
            global_var_list = self._session.state['global_var_list']

        template_card = {
            'card_type': 'button_interaction',
            'source': {
                'desc': 'JOB',
                'desc_color': 1
            },
            'main_title': {
                'title': f'JOB执行方案_{job_plan_name}'
            },
            'task_id': str(int(time.time() * 100000)),
            'sub_title_text': '参数确认',
            'horizontal_content_list': global_var_list,
            'button_list': [
                {
                    "text": "执行",
                    "style": 1,
                    "key": f"bk_job_plan_execute|{job_plan_id}|{job_plan_name}|{json.dumps(global_var_list)}"
                },
                {
                    "text": "修改",
                    "style": 2,
                    "key": f"bk_job_plan_update|{job_plan_id}|{job_plan_name}|{json.dumps(global_var_list)}"
                },
                {
                    "text": "取消",
                    "style": 3,
                    "key": f"bk_job_plan_cancel|{job_plan_name}"
                }
            ]
        }
        return template_card

    async def execute_task(self, job_plan_id: Union[str, int], global_var_list: List) -> bool:
        try:
            await JOB().execute_job_plan(
                bk_biz_id=self.biz_id,
                job_plan_id=int(job_plan_id),
                global_var_list=global_var_list,
                bk_username=self.user_id
            )
            msg = f'{job_plan_id} {global_var_list} 任务启动成功'
            return True
        except ActionFailed as e:
            msg = f'{job_plan_id} {global_var_list} error: 参数有误 {e}'
        except HttpFailed as e:
            msg = f'{job_plan_id} {global_var_list} error: 第三方服务异常 {e}'
        finally:
            # OrmClient().add()
            logger.info(msg)

        return False

    def render_job_plan_execute_msg(self, result, job_plan_name, global_var_list) -> Dict:
        return self.render_execute_msg('JOB', result, job_plan_name, global_var_list, BK_JOB_DOMAIN)
