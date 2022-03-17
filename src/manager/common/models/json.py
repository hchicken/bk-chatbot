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

from django.db import models


class DictCharField(models.TextField):
    """
    自定义字段
    """

    def get_prep_value(self, value: dict) -> str:
        """
        将py对象转换为数据库对象
        """
        return json.dumps(value)

    def to_python(self, value: str):
        if value is None:
            return value

        return json.loads(value)

    def from_db_value(self, value, expression, connection):
        """
        将数据库返回的值转换为py对象
        """
        return self.to_python(value)
