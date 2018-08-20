#!/usr/bin/env python
# -*- coding=utf-8 -*-

'''
Created on 2018年05月31日

@author: Administrator
'''

import tester_config
import utils
from api_web_base import WebBaseApi
      
class LoginApi(WebBaseApi):
    def __init__(self, debug = 1):
        super(LoginApi, self).__init__(debug=debug)
                          
    @property
    def account(self):
        return self.__account
    
    @account.setter
    def account(self, account):
        self.__account = account
        
    @property
    def pwd(self):
        return self.__pwd
     
    @pwd.setter
    def pwd(self, pwd):
        self.__pwd = pwd
        
    def __str__(self, *args, **kwargs):
        return str({'account': self.__account, 'pwd': self.__pwd})
    
    def login(self, account, pwd):
        self.__account = account
        self.__pwd = pwd
        
        ok = self.__user_login('/user/login')
        if ok:
            self.__app_setting('/app/setting')
            self.__upload_getToken('/upload/getToken')
            
        return ok
    
    def __user_login(self, method):
        params = {'phone':self.__account, 'pwd':utils.webRsaEncrypt(self.__pwd)}
        code, result = self.post(method=method, usetoken=False, params=params)
        if code == 1 or code == 0:
            tester_config.login_result_data = result
            print(tester_config.login_result_data)
            return True
        else:
            print('[code: %d result:%s]' % (code, result))
            
        return False
    
    def __upload_getToken(self, method):
        params = {'uid':tester_config.login_result_data['uid']}
        code, result = self.post(method=method, usetoken=True, params=params)
        if (code == 1) or (code == 0):
            print(result)
        else:
            print('[code: %d result:%s]' % (code, result))
            
    def __app_setting(self, method):
        params = {'uid':tester_config.login_result_data['uid']}
        code, result = self.post(method=method, usetoken=True, params=params)
        if (code == 1) or (code == 0):
            print(result)
        else:
            print('[code: %d result:%s]' % (code, result))
            
if __name__ == '__main__':
    debug = 1
    login = LoginApi(debug=debug)
    login.account = tester_config.account
    login.pwd = tester_config.pwd
    print(login)
    if login.login(tester_config.account, tester_config.pwd):
        pass
