import os
import sys
import socket
import ujson
import json
import time

try:
    import struct as ustruct
except:
    import ustruct

try:
    import binascii as ubinascii
except:
    import ubinascii

import urllib

try:
    from urllib import request as urequest
except:
    from urllib import urequest

import logging

logging.basicConfig(level=logging.DEBUG)

log = logging.getLogger('liwei')

os.getcwd()
os.listdir()
#if os.path.isfile('./ds3231.py'):
#    os.remove('ds3231.py')
os.listdir()

def test():
    d = {'a':111, 'c':111, 'd':222, 'e':'sdfsdfsdfdsfsdfsdfdsfsdfryjjkljklk;l;liytytyutyutyutyutu'}
    s = ujson.dumps(d)
    print(s)
    s1 = ujson.loads(s)
    print(s1)
    
def test1():
    d = {'a':111, 'c':111, 'd':222, 'e':'sdfsdfsdfdsfsdfsdfdsfsdfryjjkljklk;l;liytytyutyutyutyutu'}
    s = json.dumps(d)
    print(s)
    s1 = json.loads(s)
    print(s1)
    
if __name__ == '__main__':
    print(time.time())
    print(time.time())
    
    test()
    test1()
    
    v = ustruct.pack('hhl', 1, 2, 3)
    print(v)
    
    v1 = ubinascii.b2a_base64(bytes('0123456789', 'utf8'))
    print(v1)
        
    print(bin(1)[2:])
    print(bin(2)[2:])
    print(bin(1 | 2)[2:])
    print(1 >> 2)
    
    log.debug('111111111111111111111111')
    log.debug('111111111111111111111111')
    log.debug('111111111111111111111111')
    
    print('----------------------------------------------------')
    with urequest.urlopen('http://www.baidu.com') as f:
        data  = f.read()
        print('Status:', f.status, f.reason)
        
        for k, v in f.getheaders():
            print('%s:%s' % (k, v))
        print('Data:', data)
        
