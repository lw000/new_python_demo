#!/usr/bin/env python
# -*- coding=utf-8 -*-

'''
Created on 2017年 12月15日

@author: Administrator
'''

import redis

import _thread
import threading
import time
import json
import queue
import logging
import schedule

from RedisHelper import RedisHelper
from cffi.api import basestring

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s %(filename)s[line:%(lineno)d]',
                    datefmt='%a, %d %b %Y %H:%M:%S')

taskQueue = queue.Queue()

def pushServer():
    redis = RedisHelper(host='127.0.0.1', port=6379)
    data = {'name': 'liwei', 'age': '30', 'sex': '1', 'addr': '深圳市南山区'}
    
    while True:
        j = json.dumps(data, ensure_ascii=False)
        redis.publish(j)  # 发布
        
        break
        
        
def radis_push_server_minute():
    redis = RedisHelper(host='127.0.0.1', port=6379)
    data = {'name': 'liwei', 'age': '30', 'sex': '1', 'addr': '深圳市南山区'}
    
    while True:       
        j = json.dumps(data, ensure_ascii=False)
        redis.publish(j)  # 发布
        
        break

def recvedServer(q):
    redis = RedisHelper()
    redis_sub = redis.subscribe()  # 调用订阅方法
    
    while True:
        msg = redis_sub.parse_response()
        if msg:
            q.put(msg)

class Worker(threading.Thread):
    def __init__(self, q, name):
        self.__quit = False
        self.__q = q
        super(Worker, self).__init__(name=name)

    def quitWorker(self):
        self.__quit = True

    def run(self):
        threading.Thread.run(self)
        while not self.__quit:
            data = self.__q.get()
#             if isinstance(data[0], basestring):
            print('%s: %s' % (self.name, data[0].decode('utf8')))
#             if isinstance(data[1], basestring):
            print('%s: %s' % (self.name, data[1].decode('utf8')))
#             if isinstance(data[2], basestring):
            print('%s: %s' % (self.name, data[2].decode('utf8')))


def worker_server(q, name):
    while True:
        data = q.get()
#         if isinstance(data[0], basestring):
        print('%s: %s' % (name, data[0].decode('utf8')))
#         if isinstance(data[1], basestring):
        print('%s: %s' % (name, data[1].decode('utf8')))
#         if isinstance(data[2], basestring):
        print('%s: %s' % (name, data[2].decode('utf8')))

def main():
#     pool = redis.ConnectionPool(host='192.168.204.128', port=6379)
    pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
    r = redis.Redis(connection_pool=pool)
    r.set('liwei', '20')
    print(r.get('liwei').decode())

    try:
#         _thread.start_new_thread(pushServer, ('pushServer',))
        
        schedule.every().seconds.do(pushServer)
        schedule.every().minute.do(radis_push_server_minute, ('radis_push_server_minute'))
        schedule.every().hour.do(radis_push_server_minute, ('radis_push_server_minute'))
        
        t = threading.Thread(target=recvedServer,
                             name='recvedServer', args=(taskQueue,))
        t.start()

        worker1 = Worker(taskQueue, 'worker1')
        worker1.start()

        worker2 = Worker(taskQueue, 'worker2')
        worker2.start()

        while True:
            schedule.run_pending()
#             time.sleep(1)
            
    except:
        print('error: unable to start thread')


if __name__ == '__main__':
    main()
