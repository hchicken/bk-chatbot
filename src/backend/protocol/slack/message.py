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

from typing import (
    Iterable, Tuple, Union, List, Dict, Optional,
    Callable
)

from opsbot.adapter import (
    Message as BaseMessage, MessageSegment as BaseMessageSegment,
    MessageTemplate as BaseMessageTemplate
)
from opsbot.stdlib import escape, unescape


class MessageSegment(BaseMessageSegment):
    def __delitem__(self, key):
        pass

    def __str__(self):
        if self.is_text():
            return escape(self.data.get('text', ''), escape_comma=False)

        params = ','.join(('{}={}'.format(k, escape(str(v)))
                           for k, v in self.data.items()))
        if params:
            params = ',' + params
        return '[W:{type}{params}]'.format(type=self.type, params=params)

    def is_text(self) -> bool:
        return self.type == 'text'

    @staticmethod
    def text(text: str):
        return MessageSegment(type_='text', data={'text': text})


class Message(BaseMessage):
    @staticmethod
    def _normalized(msg_str: str) -> Iterable[MessageSegment]:
        def iter_function_name_and_extra() -> Iterable[Tuple[str, str]]:
            yield 'text', unescape(msg_str)

        for function_name, extra in iter_function_name_and_extra():
            if function_name == 'text':
                if extra:
                    # only yield non-empty text segment
                    yield MessageSegment(type_=function_name,
                                         data={'text': extra})
            else:
                data = {k: v for k, v in map(
                    lambda x: x.split('=', maxsplit=1),
                    filter(lambda x: x, (x.lstrip() for x in extra.split(',')))
                )}
                yield MessageSegment(type_=function_name, data=data)


class MessageTemplate(BaseMessageTemplate):
    @classmethod
    def render_markdown_msg(cls, title: str, content: str) -> Dict:
        def normalize(text: str) -> str:
            text = text.replace('<bold>', '')
            text = text.replace('<warning>', '`')
            text = text.replace('<info>', '')
            return text

        # todo adapt more attribute
        return {
            "attachments": [
                {
                    "color": "#2eb886",
                    "title": normalize(title),
                    "title_link": "",
                    "text": normalize(content),
                    "footer": "bkchat",
                    "footer_icon": "",
                }
            ]
        }

    @classmethod
    def render_welcome_msg(cls, data: List, bk_biz_id: Union[int, str]) -> Dict:
        data = [
            {
                'value': str(biz['bk_biz_id']), 'text': biz['bk_biz_name']
            } for biz in data
        ]

        return {
            'text': '*BKCHAT*',
            'attachments': [
                {
                    'title': '欢迎使用蓝鲸信息流',
                    'callback_id': 'bk_chat_common_callback|slack_select_bk_biz_id',
                    'color': '3AA3E3',
                    'attachment_type': 'default',
                    'actions': [
                        {
                            "name": "业务",
                            "text": "请选择业务",
                            "type": "select",
                            'selected_options': [
                                {
                                    'text': biz['text'],
                                    'value': biz['value']
                                } for biz in data if biz['value'] == str(bk_biz_id)
                            ][:1],
                            "options": data
                        }
                    ]
                },
                {
                    'text': '请选择应用',
                    'color': '3AA3E3',
                    'callback_id': 'bk_chat_common_callback|slack_select_bk_app',
                    'actions': [
                        {
                            "name": "task",
                            "text": "CI",
                            "type": "button",
                            "value": "bk_devops"
                        },
                        {
                            "name": "task",
                            "text": "JOB",
                            "type": "button",
                            "value": "bk_job"
                        },
                        {
                            "name": "task",
                            "text": "SOPS",
                            "type": "button",
                            "value": "bk_sops"
                        },
                        {
                            "name": "task",
                            "text": "ITSM",
                            "type": "button",
                            "value": "bk_itsm"
                        }
                    ]
                }
            ]
        }

    @classmethod
    def render_biz_list_msg(cls, data: List):
        data = [
            {
                'value': str(biz['bk_biz_id']), 'text': biz['bk_biz_name']
            } for biz in data
        ]
        return {
            'text': '*BKCHAT*',
            'attachments': [
                {
                    'title': '业务绑定',
                    'callback_id': 'bk_cc_biz_select',
                    'color': '3AA3E3',
                    'attachment_type': 'default',
                    'actions': [
                        {
                            "name": "业务",
                            "text": "请选择业务",
                            "type": "select",
                            "options": data
                        }
                    ]
                }
            ]
        }

    @classmethod
    def render_task_list_msg(cls,
                             platform: str,
                             title: str,
                             desc: str,
                             question_key: str,
                             data: List,
                             submit_key: str,
                             submit_text: str = '确认',
                             render: Callable = None):
        if not data:
            return None

        if render:
            data = [render(x) for x in data]

        data = [
            {
                'value': str(task['id']), 'text': task['text'], 'name': question_key
            } for task in data
        ]

        return {
            'text': f'*{platform}*',
            'attachments': {
                'title': title,
                'text': desc,
                'callback_id': submit_key,
                'color': '3AA3E3',
                'attachment_type': 'default',
                'actions': [
                    {
                        "name": "业务",
                        "text": "请选择实例",
                        "type": "select",
                        "options": data
                    }
                ]
            }
        }

    @classmethod
    def render_task_select_msg(cls):
        pass

    @classmethod
    def render_task_execute_msg(cls):
        pass

    @classmethod
    def render_task_filter_msg(cls):
        pass


class MessageParser:
    @classmethod
    def parse_select(cls, ctx: Dict) -> Optional[str]:
        try:
            for actions in ctx['actions']:
                for select_action in actions:
                    return select_action['value']
        except KeyError:
            return None
