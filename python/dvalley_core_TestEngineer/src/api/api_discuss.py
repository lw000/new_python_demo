#!/usr/bin/env python
# -*- coding=utf-8 -*-

'''
Created on 2018年05月31日

@author: Administrator
'''

import tester_config
from api_web_base import WebBaseApi

class DiscussApi(WebBaseApi):
    def __init__(self, debug = 1):
        super(DiscussApi, self).__init__(debug=debug)
                
    def start(self):
        self.__discuss_getTags(method='/discuss/getTags')
        self.__discuss_list(method='/discuss/list')
        self.__discuss_detail(method='/discuss/detail')
        self.__discuss_myDiscuss(method='/discuss/myDiscuss')
                
    def stop(self):
        pass
     
    def __discuss_getTags(self, method):
        params = {'uid':tester_config.login_result_data['uid']}
        code, result = self.post(method=method, usetoken=True, params=params)  
        if (code == 1) or (code == 0):
            print(result)
        else:
            print('[code: %d result:%s]' % (code, result))
    
    def __discuss_list(self, method):
        params = dict(uid=tester_config.login_result_data['uid'], type=0, area_code=0, v_id=0, page=1, limit=20, first_id=0, last_id=0)
        code, result = self.post(method=method, usetoken=True, params=params)
        
        if (code == 1) or (code == 0):
            print(result)
        else:
            print('[code: %d result:%s]' % (code, result))
                            
    def __discuss_detail(self, method):
        params = dict(uid=tester_config.login_result_data['uid'], discuss_id=48585)
        
        code, result = self.post(method=method, usetoken=True, params=params)  
        if (code == 1) or (code == 0):
            print(result)
        else:
            print('[code: %d result:%s]' % (code, result))
        
    def __discuss_myDiscuss(self, method):
        params = dict(uid=tester_config.login_result_data['uid'], to_uid=tester_config.login_result_data['uid'], type=0, limit=20, page=1)
        
        code, result = self.post(method=method, usetoken=True, params=params)  
        if (code == 1) or (code == 0):
            print(result)
        else:
            print('[code: %d result:%s]' % (code, result))
            
            
if __name__ == '__main__': 
    from api_login import LoginApi
    login = LoginApi(debug=1)
    login.account = tester_config.account
    login.pwd = tester_config.pwd
    if login.login(tester_config.account, tester_config.pwd):
        tester = DiscussApi(debug=1)
        tester.start()
        tester.stop() 
