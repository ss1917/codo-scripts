#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Contact : 191715030@qq.com
Author  : shenshuo
Date    : 2018/12/25
Desc    : 优化并集中管理
"""

import requests
import json
from settings import api_settings


class API(object):
    def __init__(self):
        self.__token = api_settings['publish_token']
        self.publish_info_api = api_settings.get('publish_info_api')
        self.get_key_api = api_settings.get('get_key_api')
        self.mail_api = api_settings.get('mail_api')

    def get_publish_name_info(self, publish_name):
        try:
            params = {'key': 'publish_name', 'value': publish_name}
            res = requests.get(self.publish_info_api, params=params, cookies=dict(auth_key=self.__token))
            ret = json.loads(res.content)
            if ret['code'] == 0: return ret['data']
        except Exception as e:
            print('[Error:] Publish发布接口连接失败，错误信息：{}'.format(e))
            exit(-2)

    def get_publish_all_info(self):
        '''获取发布配置所有信息'''

        res = requests.get(self.publish_info_api, cookies=dict(auth_key=self.__token))
        ret = json.loads(res.content)
        if ret['code'] == 0: return ret['data']

    def get_api_info(self, api_url):
        '''获取接口所有信息'''

        res = requests.get(api_url, cookies=dict(auth_key=self.__token))
        ret = json.loads(res.content)
        return ret['data']

    def send_mail_for_api(self, mail_list, mail_subject, mail_content):
        """发送邮件"""

        req1 = requests.get(self.get_key_api, cookies=dict(auth_key=self.__token))
        if req1.status_code != 200:
            raise SystemExit(req1.status_code)

        ret1 = json.loads(req1.text)
        if ret1['code'] == 0:
            csrf_key = ret1['csrf_key']
        else:
            raise SystemExit(ret1['code'])

        body = json.dumps({"to_list": mail_list, "subject": mail_subject, "content": mail_content, "subtype": "plain"})
        res = requests.post(self.mail_api, data=body, cookies=dict(auth_key=self.__token, csrf_key=csrf_key))
        if res.status_code != 200:
            raise SystemExit(res.status_code)
        else:
            return json.loads(res.text)['msg']
