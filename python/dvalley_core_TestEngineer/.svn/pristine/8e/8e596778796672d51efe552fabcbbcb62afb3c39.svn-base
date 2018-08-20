#!/usr/bin/env python
# -*- coding=utf-8 -*-

'''
Created on 2018年05月31日

@author: Administrator
'''

import tester_config
from api_net_base import BaseHttpApi 
        
class WebBaseApi(object):
    def __init__(self, debug = 1):
        self.__host = tester_config.host(tester_config.API_WEB, debug)
        self.__http = BaseHttpApi(self.__host, tester_config.API_WEB)
        
    def post(self, method, usetoken, params):
        result = self.__http.post(method, usetoken, params)
        code = result['result']
        if code == 1:
            return (code, result['data'])
        elif code == 0:
            return (code, result['error'])
        else:
            return (code, {'error': 'error'})
                
    def get(self, url, params):   
        result = self.__http.get(url, params)
        code = result['result']
        if code == 1:
            return (code, result['data'])
        elif code == 0:
            return (code, result['error'])
        else:
            return (code, {'error': 'error'})
    