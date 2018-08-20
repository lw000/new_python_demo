#!/usr/bin/env python
# -*- coding=utf-8 -*-

'''
Created on 2018年05月31日

@author: Administrator
'''

import sys
import time

PLATFORM = 'x64'
if PLATFORM == 'x64':
    sys.path.append(r'./x64')
else:
    sys.path.append(r'./x86')
    
# sys.path.append('dvalley_core_python_ext.pyd')

# import dvalley_core_python_ext

import dvalley_core_python_ext

def webRsaEncrypt(s):
    return dvalley_core_python_ext.rsaEncrypt(10000, s)

def webSignWithJson(s, slat = ''):
    return dvalley_core_python_ext.signWithJson(10000, s, slat)

def webSignWithString(s, slat = ''):
    return dvalley_core_python_ext.signWithString(10000, s, slat)

def redbagRsaEncrypt(s):
    return dvalley_core_python_ext.rsaEncrypt(10001, s)

def redbagSignWithJson(s, slat = ''):
    return dvalley_core_python_ext.signWithJson(10001, s, slat)

def redbagSignWithString(s, slat = ''):
    return dvalley_core_python_ext.signWithString(10001, s, slat)

def thirdPartRsaEncrypt(s):
    return dvalley_core_python_ext.rsaEncrypt(10002, s)

def thirdPartSignWithJson(s, slat = ''):
    return dvalley_core_python_ext.signWithJson(10002, s, slat)

def thirdPartSignWithString(s, slat = ''):
    return dvalley_core_python_ext.signWithString(10002, s, slat)

if __name__ == '__main__':
    import demjson
    import ujson
    import rapidjson
    
    pload = dict(token='c4c6579b81b47c7524bd89cc526c9007',
                lang=1,
                device_id='40C875E5-1193-4EBC-8350-CADB42437F81',
                uid='',
                app_version='3.0.2',
                client_type='iOS',
                host=0)
    
#     print(webRsaEncrypt('1111111111'))
#     pload = {'a':'1111111111', 'time_stamp': int(time.time())}
#     print(webSignWithJson(demjson.encode(pload)))
#     print(webSignWithString('1111111111'))
    
    print(sorted(pload.keys()))
    
    count = 10000
    tp = 0
    for i in range(count):
        t = time.clock()
        str = rapidjson.dumps(pload)
        t1 = time.clock()
        tp = tp + (t1-t)
    print("rapidjson pload t:%f %s" % (tp/count, str))
    
    tp = 0
    for i in range(count):
        t = time.clock()
        str = ujson.dumps(pload)
        t1 = time.clock()
        tp = tp + (t1-t)
    print("ujson pload t:%f %s" % (tp/count, str))
    
#     tp = 0
#     for i in range(count):
#         t = time.clock()
#         str = demjson.encode(pload)
#         t1 = time.clock()
#         tp = tp + (t1-t)
#     print("demjson pload t:%f %s" % (tp/count, str))
    
    t = time.clock()
    s = redbagRsaEncrypt(str)
    t1 = time.clock()
    print("redbagRsaEncrypt t:%f %s" % (t1-t, s))
    
    t = time.clock()
    s = redbagSignWithString(str)
    t1 = time.clock()
    print("redbagSignWithString t:%f %s" % (t1-t, s))
    
    t = time.clock()
    s = redbagSignWithJson(str)
    t1 = time.clock()
    print("redbagSignWithJson t:%f %s" % (t1-t, s))
    
#     print(thirdPartRsaEncrypt('1111111111'))
#     pload = {'a':'1111111111', 'time_stamp': int(time.time())}
#     print(thirdPartSignWithJson(demjson.encode(pload)))
#     print(thirdPartSignWithString('1111111111'))

