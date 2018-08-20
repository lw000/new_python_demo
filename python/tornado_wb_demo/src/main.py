# -*- coding: UTF-8 -*-

'''
Created on 2017年1月22日

@author: Administrator
'''

import os
import signal
import logging
import tornado
from tornado.ioloop import IOLoop
from tornado.web import Application

from web_handler import DefaultHandler
from web_handler import DhtHandler
from web_handler import DistanceHandler
from web_handler import AddHandler
from web_handler import SubHandler
from web_handler import MulHandler

logger = logging.getLogger()
fm = tornado.log.LogFormatter(fmt='[%(asctime)s]%(color)s[%(levelname)s]%(end_color)s[(module)s:%(lineno)d] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
tornado.log.enable_pretty_logging(logger=logger)
logger.handlers[0].setFormatter(fm)
     
class ServerApplication(Application):
    def __init__(self):
        self.handlers = ([
            ('/', DefaultHandler),
            ('/dht', DhtHandler),
            ('/distance', DistanceHandler),
            ('/add', AddHandler),
            ('/sub', SubHandler),
            ('/mul', MulHandler),
        ])
        
        self.settings = dict(
#             cookie_secret='C7B1AFCC-810E-46d0-8157-09FC488D4C71',
            template_path=os.path.join(os.path.dirname(__file__), 'templates'),
            static_path=os.path.join(os.path.dirname(__file__), 'static'),
#             xsrf_cookies=True,
        )
        
        super(ServerApplication, self).__init__(self.handlers, **self.settings)

def handle_sign(sig, frame):
    IOLoop.current().add_callback_from_signal(IOLoop.current().stop, sig, frame)

if __name__ == '__main__':
    
    signal.signal(signal.SIGINT, handle_sign)
    
    app = ServerApplication()
    port = 8006
    app.listen(port)
    print('start listen [%d]' % (port))
    IOLoop.current().start()
