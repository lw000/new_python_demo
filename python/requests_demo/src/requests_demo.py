#!/usr/bin/env python
# -*- coding=utf-8 -*-

'''
Created on 2018年5月17日

@author: Administrator
'''

import requests
import json
import demjson
import threading
import time
import signal

quit_worker = 0

def get_add_test(host):
    payload = {'a': 1, 'b': 2}
    url = host + '/add'
    r = requests.get(url, params=payload);
#     print(r)
    print(r.url)
    print(r.text)
    if(r.status_code == 200):
        data = demjson.decode(r.text)
        print(data['code'])
        print(data['msg'])
        print(data['data']['result'])
      
def post_add_test(host):
    payload = {'a': 4, 'b': 5}
    url = host + '/add'
    r = requests.post(url, data=payload);
#     print(r)
    print(r.url)
    print(r.text)
    if(r.status_code == 200):
        data = demjson.decode(r.text)
        print(data['code'])
        print(data['msg'])
        print(data['data']['result'])
        
def post_register_test(host):
    url = host + '/register'
    payload = {'username': '1111111', 'password': '22222'}
    r = requests.post(url, data=payload);
#     print(r)
    print(r.url)
    print(r.text)
    if(r.status_code == 200):
        data = json.loads(r.text)
        print(data['code'])
        print(data['msg'])
        print(data['data']['uid'])
    
class TestWorker(threading.Thread):
    
    def __init__(self, name):
        super(TestWorker, self).__init__(name=name)
    
    def run(self):
        threading.Thread.run(self)
        while quit_worker == 0:
            if 1: 
                get_add_test('http://127.0.0.1:8006')
                post_add_test('http://127.0.0.1:8006')
#                 get_add_test('http://192.168.204.128:8006')
#                 post_add_test('http://192.168.204.128:8006')
            else:
                get_add_test('http://47.52.164.140:8006')
                post_add_test('http://47.52.164.140:8006')
                         
            time.sleep(1)
            
        print('worker over.')

def handle_sigchld(signum, frame):
    print('Received signal: ', signum)
    quit_worker = 1
            
if __name__ == '__main__':
    signal.signal(signal.SIGINT, handle_sigchld)
    
    res = requests.get('http://mobile.weather.com.cn/data/forecast/101010100.html?_=1381891660081')
    print(res.text)
    
#     worker = TestWorker('worker')
#     worker.start()
#     worker.join()
    