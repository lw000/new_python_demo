'''
Created on 2018年1月3日

@author: Administrator
'''

import redis

class RedisHelper(object):
    def __init__(self, host='127.0.0.1', port=6379):
#         self.__pool = redis.ConnectionPool(host='192.168.204.128', port=6379)
        self.__pool = redis.ConnectionPool(host=host, port=port)
        self.__conn = redis.Redis(connection_pool=self.__pool)
        self.__default_channel = 'monitor_main'  # 定义名称

    # 定义发布方法
    def publish(self, msg):
        v = self.__conn.publish(self.__default_channel, msg)
        return v

    # 定义订阅方法
    def subscribe(self):
        p = self.__conn.pubsub()
        p.subscribe(self.__default_channel)
        return p

    # 定义发布方法
    def publishChannel(self, channel, msg):  
        v = self.__conn.publish(channel, msg)
        return v

    # 定义订阅方法
    def subscribeChannel(self, channel):
        p = self.__conn.pubsub()
        p.subscribe(channel)
        p.parse_response()
        return p
