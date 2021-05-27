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
 * @file 按需引入 bk-magic-vue 组件
 * @author
 */

/* eslint-disable import/no-duplicates */

import Vue from 'vue'

import {
    bkBadge, bkButton, bkCheckbox, bkCheckboxGroup, bkCol, bkCollapse, bkCollapseItem, bkContainer, bkDatePicker,
    bkDialog, bkDropdownMenu, bkException, bkForm, bkFormItem, bkInfoBox, bkInput, bkLoading, bkMemberSelector, bkMessage,
    bkNavigation, bkNavigationMenu, bkNavigationMenuItem, bkNotify, bkOption, bkOptionGroup, bkPagination,
    bkPopover, bkProcess, bkProgress, bkRadio, bkRadioGroup, bkRoundProgress, bkRow, bkSearchSelect, bkSelect,
    bkSideslider, bkSlider, bkSteps, bkSwitcher, bkTab, bkTabPanel, bkTable, bkTableColumn, bkTagInput, bkPopconfirm,
    bkTimePicker, bkTimeline, bkTransfer, bkTree, bkUpload, bkClickoutside, bkTooltips, bkSwiper, bkRate, bkAnimateNumber,
    bkVirtualScroll, bkColorPicker, bkCard
} from '@tencent/bk-magic-vue'

// bkDiff 组件体积较大且不是很常用，因此注释掉。如果需要，打开注释即可
// import { bkDiff } from '@tencent/bk-magic-vue'

// components use
Vue.use(bkBadge)
Vue.use(bkButton)
Vue.use(bkCheckbox)
Vue.use(bkCheckboxGroup)
Vue.use(bkCol)
Vue.use(bkCollapse)
Vue.use(bkCollapseItem)
Vue.use(bkContainer)
Vue.use(bkDatePicker)
Vue.use(bkDialog)
Vue.use(bkDropdownMenu)
Vue.use(bkException)
Vue.use(bkForm)
Vue.use(bkFormItem)
Vue.use(bkInput)
Vue.use(bkMemberSelector)
Vue.use(bkNavigation)
Vue.use(bkNavigationMenu)
Vue.use(bkNavigationMenuItem)
Vue.use(bkOption)
Vue.use(bkOptionGroup)
Vue.use(bkPagination)
Vue.use(bkPopover)
Vue.use(bkProcess)
Vue.use(bkProgress)
Vue.use(bkRadio)
Vue.use(bkRadioGroup)
Vue.use(bkRoundProgress)
Vue.use(bkRow)
Vue.use(bkSearchSelect)
Vue.use(bkSelect)
Vue.use(bkSideslider)
Vue.use(bkSlider)
Vue.use(bkSteps)
Vue.use(bkSwitcher)
Vue.use(bkTab)
Vue.use(bkTabPanel)
Vue.use(bkTable)
Vue.use(bkTableColumn)
Vue.use(bkTagInput)
Vue.use(bkPopconfirm)
Vue.use(bkTimePicker)
Vue.use(bkTimeline)
Vue.use(bkTransfer)
Vue.use(bkTree)
Vue.use(bkUpload)
Vue.use(bkSwiper)
Vue.use(bkRate)
Vue.use(bkAnimateNumber)
Vue.use(bkVirtualScroll)
Vue.use(bkColorPicker)
Vue.use(bkCard)

// bkDiff 组件体积较大且不是很常用，因此注释了。如果需要，打开注释即可
// Vue.use(bkDiff)

// directives use
Vue.use(bkClickoutside)
Vue.use(bkTooltips)
Vue.use(bkLoading)

// Vue prototype mount
Vue.prototype.$bkInfo = bkInfoBox
Vue.prototype.$bkMessage = bkMessage
Vue.prototype.$bkNotify = bkNotify
