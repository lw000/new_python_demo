#!/usr/bin/env python
# -*- coding=utf-8 -*-

'''
Created on 2018年05月31日

@author: Administrator
'''

import tester_config
from api_web_base import WebBaseApi

class SettingApi(WebBaseApi):
    def __init__(self, debug = 1):
        super(SettingApi, self).__init__(debug=debug)
                
    def start(self):
        self.__setting_list(method='/setting/list')
        self.__setting_set(method='/setting/set')
        
    def stop(self):
        pass
           
    def __setting_list(self, method):
        params = dict(uid=tester_config.login_result_data['uid'], name='liwei')
        
        code, result = self.post(method=method, usetoken=True, params=params) 
        if (code == 1) or (code == 0):
            print(result)
        else:
            print('[code: %d result:%s]' % (code, result))
            
    def __setting_set(self, method):
        if 1:
            params = dict(uid=tester_config.login_result_data['uid'], key='hide_location', val=0)
        else:
            params = dict(uid=tester_config.login_result_data['uid'], key='look_fans', val=0)
        
        code, result = self.post(method=method, usetoken=True, params=params) 
        if (code == 1) or (code == 0):
            print(result)
        else:
            print('[code: %d result:%s]' % (code, result))

if __name__ == '__main__': 
    from api_login import LoginApi
    debug = 1
    login = LoginApi(debug = debug)
    if login.login(tester_config.account, tester_config.pwd):
        tester = SettingApi(debug = debug)
        tester.start()
        tester.stop() 
