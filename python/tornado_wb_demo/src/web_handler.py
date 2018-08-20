# -*- coding: UTF-8 -*-

'''
Created on 2017年1月22日

@author: Administrator
'''

from tornado.web import RequestHandler
import rapidjson as json
import time

class DefaultHandler(RequestHandler):
    def get(self):
        data = {'code':0, 'msg':'你好，Python.'}
        s = json.dumps(data)
        self.write(s)

    def post(self):
        data = {'code':0, 'msg':'你好，Python'}
        s = json.dumps(data)
        self.write(s)        
        
class DhtHandler(RequestHandler):
    def get(self):
        c = self.get_argument('count', '-1')
        t = self.get_argument('temp', '-1')
        h = self.get_argument('hum', '-1')
        print('统计次数：%s, 温度：%s, 湿度：%s' % (c, t, h))
        self.write('YES')

    def post(self):
        self.write('YES')
        
class DistanceHandler(RequestHandler):
    def get(self):
        d = self.get_argument('distance')
        print('距离：%s cm' % (d))    
        self.write('YES')

    def post(self):    
        self.write('YES')
        
        
class AddHandler(RequestHandler):
    def __add(self, a, b):
        c = a + b
        data = {'code':0, 'msg':'ok', 'data': {'result':c, 'timestamp:':int(time.time())}}
        s = json.dumps(data)
        return s
    
    def get(self):
        a = self.get_argument('a')
        b = self.get_argument('b')
        json = self.__add(int(a), int (b))
        self.write(json)

    def post(self):
        a = self.get_argument('a')
        b = self.get_argument('b')
        json = self.__add(int(a), int (b))
        self.write(json)
        
class SubHandler(RequestHandler):
    def __sub(self, a, b):
        c = a - b
        data = {'code':0, 'msg':'ok', 'data': {'result':c, 'timestamp:':int(time.time())}}
        s = json.dumps(data)
        return s
    
    def get(self):
        a = self.get_argument('a')
        b = self.get_argument('b')
        json = self.__sub(int(a), int (b))
        self.write(json)

    def post(self):    
        a = self.get_body_argument('a')
        b = self.get_body_argument('b')
        json = self.__sub(int(a), int (b))
        self.write(json)


class MulHandler(RequestHandler):
    def __mul(self, a, b):
        c = a * b
        data = {'code':0, 'msg':'ok', 'data': {'result':c, 'timestamp:':int(time.time())}}
        s = json.dumps(data)
        return s
    
    def get(self):
        a = self.get_argument('a')
        b = self.get_argument('b')
        json = self.__mul(int(a), int (b))
        self.write(json)

    def post(self):    
        a = self.get_body_argument('a')
        b = self.get_body_argument('b')
        json = self.__mul(int(a), int (b))
        self.write(json)