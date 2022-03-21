# -*- coding: utf-8 -*-
from django.conf import settings

BK_PAAS_HOST = settings.PAAS_API_HOST

ESB_PREFIX = "/api/c/compapi/"
ESB_PREFIX_V2 = "/api/c/compapi/v2/"

# IEOD版本ESB前辍
BK_PAAS_HOST_IEOD = settings.PAAS_API_HOST_IEOD
ESB_PREFIX_IEOD = "/component/compapi/"

# 蓝鲸平台模块域名
JOB_APIGATEWAY_ROOT = BK_PAAS_HOST_IEOD + ESB_PREFIX_IEOD + "job/"
BK_LOGIN_APIGATEWAY_ROOT = BK_PAAS_HOST + ESB_PREFIX + "bk_login/"
BK_PAAS_APIGATEWAY_ROOT = BK_PAAS_HOST + ESB_PREFIX + "bk_paas/"
CC_APIGATEWAY_ROOT = BK_PAAS_HOST + ESB_PREFIX + "cc/"

CC_APIGATEWAY_ROOT_V2 = BK_PAAS_HOST_IEOD + ESB_PREFIX_V2 + "cc/"
GSE_APIGATEWAY_ROOT_V2 = BK_PAAS_HOST + ESB_PREFIX_V2 + "gse/"
ESB_APIGATEWAY_ROOT_V2 = BK_PAAS_HOST + ESB_PREFIX_V2 + "esb/"
SOPS_APIGATEWAY_ROOT_V2 = BK_PAAS_HOST_IEOD + ESB_PREFIX_V2 + "sops/"
JOB_APIGATEWAY_ROOT_V2 = BK_PAAS_HOST_IEOD + ESB_PREFIX_V2 + "job/"
MONITOR_APIGATEWAY_ROOT = settings.BKMONITOR_APIGW + "/"
OLD_MONITOR_APIGATEWAY_ROOT = BK_PAAS_HOST + ESB_PREFIX_V2 + "monitor/"
JOB_APIGATEWAY_ROOT_V3 = BK_PAAS_HOST_IEOD + ESB_PREFIX_V2 + "jobv3/"
USER_MANAGE_APIGATEWAY_ROOT = BK_PAAS_HOST + ESB_PREFIX_V2 + "usermanage/"

# 数据平台后台接口 V3
BKDATA_APIGW = settings.BKDATA_APIGW
SOPS_APIGW = settings.SOPS_APIGW
BKDATA_ESB_PREFIX = "/v3/"

AUTH_APIGATEWAY_ROOT = BKDATA_APIGW + BKDATA_ESB_PREFIX + "auth/"
META_APIGATEWAY_ROOT = BKDATA_APIGW + BKDATA_ESB_PREFIX + "meta/"
DATAQUERY_APIGATEWAY_ROOT = BKDATA_APIGW + BKDATA_ESB_PREFIX + "dataquery/"
ACCESS_APIGATEWAY_ROOT = BKDATA_APIGW + BKDATA_ESB_PREFIX + "access/"
STOREKIT_APIGATEWAY_ROOT = BKDATA_APIGW + BKDATA_ESB_PREFIX + "storekit/"
DATABUS_APIGATEWAY_ROOT = BKDATA_APIGW + BKDATA_ESB_PREFIX + "databus/"

# 日志平台后台接口
LOG_SEARCH_PREFIX = "/"
LOG_SEARCH_APIGW = settings.LOG_SEARCH_APIGW
LOG_SEARCH_APIGATEWAY_ROOT = LOG_SEARCH_APIGW + LOG_SEARCH_PREFIX

# 节点管理
BK_NODE_APIGATEWAY_ROOT = settings.NODEMAN_APIGW + "/"

# 云石ESB接口
CSTONE_ESB_URL = settings.CSTONE_ESB_URL

# 蓝盾接口
DEVOPS_APIGW = settings.DEVOPS_APIGW

# ITSM接口
BK_ITSM_APIGW = settings.BK_ITSM_APIGW

# bkchat接口
BK_CHAT_APIGW = settings.BK_CHAT_APIGW