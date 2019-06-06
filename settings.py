#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/24 16:57
# @Author  : Fred Yang
# @File    : settings.py
# @Role    : 发布配置信息


# 系统配置中的API地址,网关地址
api_gw = 'http://gw.shinezone.net.cn/api'
mail_api = '{}/mg/v2/notifications/mail/'.format(api_gw)
login_api = '{}/accounts/login/'.format(api_gw)
publish_info_api = '{}/task/other/v2/task_other/publish_cd/'.format(api_gw)
docker_registry_info_api = '{}/task/other/v2/task_other/docker_registry/'.format(api_gw)
get_key_api = '{}/task/v2/task/accept/'.format(api_gw)

publish_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NTQ4MzU0NzYsIm5iZiI6MTU1OTc5NTQ1NiwiaWF0IjoxNTU5Nzk1NDY2LCJpc3MiOiJhdXRoOiBzcyIsInN1YiI6Im15IHRva2VuIiwiaWQiOiIxNTYxODcxODA2MCIsImRhdGEiOnsidXNlcl9pZCI6NTYsInVzZXJuYW1lIjoicHVibGlzaCIsIm5pY2tuYW1lIjoicHVibGlzaCIsImlzX3N1cGVydXNlciI6ZmFsc2V9fQ.5pVTiw3UOmex26RELOHJmVvyn6c9yLkQyCADj0VUe9s"

api_settings = dict(
    api_gw=api_gw,
    mail_api=mail_api,
    login_api=login_api,
    publish_info_api=publish_info_api,
    get_key_api=get_key_api,
    docker_registry_info_api=docker_registry_info_api,
    publish_token=publish_token
)

sonar_domain = 'http://172.16.0.230:9000/dashboard/index/'
sonar_login = '0e8510011b3fb281d1737e13b7fdceadd6b601b4'
sonar_info =dict(
    sonar_login =sonar_login,
    sonar_domain = sonar_domain
)
cmdb_info = dict()