#!/usr/bin/env python
# -*- coding=utf-8 -*-

'''
Created on 2017年12月14日

@author: Administrator
'''

import requests
import grequests
import time
# import tqdm
from retrying import retry


@retry(stop_max_delay=10000)
def retry_test():
    print('retry test.')


def execpt_handler(req, exception):
    print('Request failed')

if __name__ == '__main__':

#     retry_test()

#     for i in tqdm.tqdm(range(1000)):
#         pass

#     v = requests.get('https://github.com/timeline.json')
#     print(v.content)
#     print(v.text)
    
    urls = [
        'http://www.baidu.com',
        'http://www.baidu.com',
        'http://www.baidu.com',
        'http://www.baidu.com',
        'http://www.baidu.com',
        'http://www.baidu.com',
        'http://www.baidu.com',
        'http://www.baidu.com',
        'http://www.baidu.com',
        'http://www.baidu.com',
        'http://www.baidu.com',
        'http://www.baidu.com',
        'http://www.baidu.com',
        'http://www.baidu.com',
        'http://www.baidu.com',
        'http://www.baidu.com',
        'http://www.baidu.com',
        'http://www.baidu.com',
        'http://www.baidu.com',
        'http://www.baidu.com',
    ]
    
    t1 = time.time()
    res = (grequests.get(u) for u in urls)
    data = grequests.imap(res, exception_handler=execpt_handler)
    t2 = time.time()
    print(t2-t1)
    
    for v in data:
        print(v)
#         print(v.url)
#         print(v.headers)
        print(v.text)
#         print(r.json())

    while True:
        time.sleep(1)
