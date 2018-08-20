#!/usr/bin/env python
# -*- coding=utf-8 -*-

'''
Created on 2018年05月31日

@author: Administrator
'''

import utils
import tester_config
from api_web_base import WebBaseApi
      
class UserApi(WebBaseApi):
    def __init__(self, debug = 1):
        super(UserApi, self).__init__(debug=debug)
                
    def start(self):
        self.__user_resetPassword(method='/user/resetPassword')
        self.__user_info(method='/user/info')
        self.__user_baseinfo(method='/user/baseinfo')
        self.__user_nearUser(method='/user/nearUser')
                
    def stop(self):
        pass
    
    def __user_resetPassword(self, method):
        params = dict(uid=tester_config.login_result_data['uid'], old_pwd=utils.webRsaEncrypt('lwstar23133'), pwd=utils.webRsaEncrypt('lwstar23133'))
        
        code, result = self.post(method=method, usetoken=True, params=params)
        if (code == 1) or (code == 0):
            print(result)
        else:
            print('[code: %d result:%s]' % (code, result))
    
    #获取用户信息
    def __user_info(self, method): 
        params = dict(uid=tester_config.login_result_data['uid'], to_uid=tester_config.login_result_data['uid'])
        
        code, result = self.post(method=method, usetoken=True, params=params)
        if (code == 1) or (code == 0):
            print(result)
        else:
            print('[code: %d result:%s]' % (code, result))
            
    #获取用户基本信息
    def __user_baseinfo(self, method):
        params = dict(uid=tester_config.login_result_data['uid'], to_uid=tester_config.login_result_data['uid'])
        
        code, result = self.post(method=method, usetoken=True, params=params)
        if (code == 1) or (code == 0):
            print(result)
        else:
            print('[code: %d result:%s]' % (code, result))
            
        #附近的用户
    def __user_nearUser(self, method):
        params = dict(uid=tester_config.login_result_data['uid'], lng='10.10', lat='10.10', sex=2, page=1, limit=20, distance=2000)
        
        code, result = self.post(method=method, usetoken=True, params=params)
        if (code == 1) or (code == 0):
            print(result)
        else:
            print('[code: %d result:%s]' % (code, result))
                    
if __name__ == '__main__':
    import sys
    import getopt
    from api_login import LoginApi
    
    opts, _ = getopt.getopt(sys.argv[1:], 'd:', ['debug'])
    
    if len(opts) > 0:
        print(opts)
        for name, value in opts:
            if name == '-d':
                debug = int(value)
                login = LoginApi(debug = debug)
                login.account = tester_config.account
                login.pwd = tester_config.pwd
                if login.login(tester_config.account, tester_config.pwd):
                    tester = UserApi(debug = debug)
                    tester.start()
                    tester.stop()
                    
    else:
        print('command line parameters (use -d 0 or -d 1)')
    
    