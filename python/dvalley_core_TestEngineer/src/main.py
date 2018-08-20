#!/usr/bin/env python
# -*- coding=utf-8 -*-

'''
Created on 2017年12月26日

@author: Administrator
'''

import sys
import threading
import getopt

sys.path.append(r'./api')
sys.path.append(r'./api/x64')
sys.path.append(r'./api/x86')

import tester_config
import api
       
class Tester(threading.Thread):
    def __init__(self, name):
        super(Tester, self).__init__(name=name)
        
        self.tester = api.TesterApi(debug=0)
        self.tester.account = tester_config.account
        self.tester.pwd = tester_config.pwd
        
    def run(self):
        threading.Thread.run(self)
      
        if self.tester.login(tester_config.account, tester_config.pwd):
            while True:    
                self.tester.start()
                self.tester.stop()
                break
      
if __name__ == '__main__':
    try:
        opts, _ = getopt.getopt(sys.argv[1:], 'u:', ['url='])
        for name, value in opts:
            if name in ('-u', '--url'):
                print('%s=%s' % (name, value))
                
        ter = Tester('tester')
        ter.start()
        ter.join()
        
    except getopt.GetoptError:
        pass
    