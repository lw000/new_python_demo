#!/usr/bin/env python
# -*- coding=utf-8 -*-

'''
Created on 2018年05月31日

@author: Administrator
'''

import tester_config
from api_web_base import WebBaseApi
      
class SocialApi(WebBaseApi):
    def __init__(self, debug = 1):
        super(SocialApi, self).__init__(debug=debug)
            
    def start(self):
        self.__social_getTags(method='/social/getTags')
                
    def stop(self):
        pass
    
    def __social_getTags(self, method):
        params = dict(uid=tester_config.login_result_data['uid'])
        
        code, result = self.post(method=method, usetoken=True, params=params)
        if (code == 1) or (code == 0):
            print(result)
        else:
            print('[code: %d result:%s]' % (code, result))
            
            
if __name__ == '__main__': 
    from api_login import LoginApi
    debug = 1
    login = LoginApi(debug = debug)
    login.account = tester_config.account
    login.pwd = tester_config.pwd
    if login.login(tester_config.account, tester_config.pwd):
        tester = SocialApi(debug = debug)
        tester.start()
        tester.stop() 