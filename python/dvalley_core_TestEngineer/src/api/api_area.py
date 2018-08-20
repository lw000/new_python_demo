#!/usr/bin/env python
# -*- coding=utf-8 -*-

'''
Created on 2018年05月31日

@author: Administrator
'''

import tester_config
from api_web_base import WebBaseApi

class AreaApi(WebBaseApi):
    def __init__(self, debug = 1):
        super(AreaApi, self).__init__(debug=debug)
            
    def start(self):
        self.__area_getProvinces(method='/area/getProvinces')
        self.__area_getCities(method='/area/getCities')
        self.__area_getCityCode(method='/area/getCityCode')
                
    def stop(self):
        pass
    
    def __area_getProvinces(self, method):
        code, result = self.post(method=method, usetoken=True, params=None)
        if (code == 1) or (code == 0):
            print(result)
        else:
            print('[code: %d result:%s]' % (code, result))
    
    def __area_getCities(self, method):
        params = {'province_id':6}
        code, result = self.post(method=method, usetoken=True, params=params)
        if (code == 1) or (code == 0):
            print(result)
        else:
            print('[code: %d result:%s]' % (code, result))
            
    def __area_getCityCode(self, method):
        code, result = self.post(method=method, usetoken=True, params=None)  
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
        tester = AreaApi(debug=1)
        tester.start()
        tester.stop()
        
