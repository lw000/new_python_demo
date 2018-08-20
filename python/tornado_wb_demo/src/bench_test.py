'''
Created on 2018年6月14日

@author: Administrator
'''

import requests
import time

if __name__ == '__main__':
    payload = dict(a=2, b=3)
    for i in range(100):
        t = time.clock()
        r = requests.post('http://127.0.0.1:8006/add', data = payload)
        t1 = time.clock()
        print('add [%.4d] [%f] %s' % (i, t1-t, r.text))
        
    for i in range(100):
        r = requests.post('http://127.0.0.1:8006/sub', data = payload)
        print('sub [%.4d] [%f] %s' % (i, t1-t, r.text))
        
    for i in range(100):
        r = requests.post('http://127.0.0.1:8006/mul', data = payload)
        print('mul [%.4d] [%f] %s' % (i, t1-t, r.text))
        
    data = input('[press any key to exit]')