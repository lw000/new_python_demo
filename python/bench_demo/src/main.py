'''
Created on 2018年6月14日

@author: Administrator
'''

import os
import random
import queue
# import requests
import threading
import time
# import rapidjson as json

TaskQueue = queue.Queue()

class Consumer(threading.Thread):
    
    def __init__(self, q, name):
        self.__q = q
        super(Consumer, self).__init__(name=name)
        
    def run(self):
        threading.Thread.run(self)
        while True:
            payload = self.__q.get()
            t = time.time()
            print('%s [%.4d] put[%f] get[%f] %f, %s' % (self._name, payload['count'], payload['t'], t, t - payload['t'], payload['data']))
            self.__q.task_done()
            
#             if self.__q.empty():
#                 break
            
        print('%s over' % (self._name))
        
class Producer(threading.Thread):
    def __init__(self, q, count, threadCount, name):
        super(Producer, self).__init__(name=name)  
        self.__q = q
        self.__count = count
        self.__threadCount = threadCount
        
    def __repr__(self):
        return '{q} {count} {threadCount}'.format(q=self.__q, count=self.__count, threadCount=self.__threadCount)
    
    def run(self):
        threading.Thread.run(self)
        
        for i in range(self.__threadCount):
            consumer = Consumer(TaskQueue, 'Consumer' + str(i))
            consumer.start()
            
        while True:
            i = 0
            while i < self.__count:
                payload = dict(count=i, t = time.time(), data=dict(a=2, b=3, c=4, d=5, e=6, f=7, g=8))
                self.__q.put(payload)
                i = i + 1
#             time.sleep(2)
            break
            
        print('%s over' % (self._name))

if __name__ == '__main__':
    d = os.path.dirname(__file__)
    p = os.path.join(d, 'x.txt')
    print(p)
    
    v = int.from_bytes(b'11', byteorder='big')
    print(v)
    v = int.from_bytes(b'11', byteorder='little')
    print(v)
    
    lst = list('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_')
    random.shuffle(lst)
    print(lst)
    
    lst.sort()
    print(lst)
    
    print(max(lst))
    print(min(lst))
    
    producer = Producer(TaskQueue, 1000000, 1, 'Producer')
    producer.start()
    producer.join()
    