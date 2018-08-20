'''
Created on 2018年6月8日

@author: Administrator
'''

from tornado import gen  #引入协程库gen
from tornado.httpclient import AsyncHTTPClient #引入框架中的异步客户端
from tornado.ioloop import IOLoop

@gen.coroutine
def cor_visit():
    http_client = AsyncHTTPClient()
    response = yield http_client.fetch('http://www.baidu.com')
    print(response.body)
    
if __name__ == '__main__':
    IOLoop.current().run_sync(lambda: cor_visit())
