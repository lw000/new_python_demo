'''
Created on 2018骞�1鏈�4鏃�

@author: Administrator
'''
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('{\'code\':0, \'what\':\'Hello, world.\'}')

    def post(self):
        self.write('{\'code\':0, \'what\':\'Hello, world.\'}')
        
        
class DhtHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('{\'code\':0, \'what\':\'Hello, world.\'}')

    def post(self):
        self.write('{\'code\':0, \'what\':\'Hello, world.\'}')