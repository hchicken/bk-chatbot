/**
 * TencentBlueKing is pleased to support the open source community by making
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
 * @file 页面公共请求即每切换 router 时都必须要发送的请求
 * @author
 */

// import store from '@/store'

// const config = {
//     fromCache: true,
//     cancelWhenRouteChange: false
// }

/**
 * 获取 user 信息
 *
 * @return {Promise} promise 对象
 */
// function getUser () {
//     return store.dispatch('userInfo', config)
// }

export default function () {
    return Promise.all([
        // getUser()
    ])
}
