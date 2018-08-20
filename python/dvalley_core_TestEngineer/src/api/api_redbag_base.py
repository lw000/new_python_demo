#!/usr/bin/env python
# -*- coding=utf-8 -*-

'''
Created on 2018年05月31日

@author: Administrator
'''

import tester_config
from api_net_base import BaseHttpApi 
        
class RedBagBaseApi(object):
    def __init__(self, debug = 1):
        self.__host = tester_config.host(tester_config.API_REDBAG, debug)
        self.__http = BaseHttpApi(self.__host, tester_config.API_REDBAG)
        
    def post(self, method, usetoken, params):
        result = self.__http.post(method, usetoken, params)
        code = result['code']
        if code == 200:
            if 'data' in result:
                return (code, result['data'])
            else:
                return (code, {'data': None})
        else:
            return (code, {'error':result})
        
    def get(self, url, params):
        result = self.__http.get(url, params)
        code = result['code']
        if code == 200:
            return (code, result['data'])
        else:
            return (code, {'error':result})