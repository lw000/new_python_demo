'''
Created on 2018年6月7日

@author: Administrator
'''

import types

account = '13632767233'
pwd = 'lwstar23133'

API_WEB = 1
API_REDBAG = 2

login_result_data = {}

def host(buniss, debug):
    host = ''
    if buniss == API_WEB: 
        if debug == 0:
            host = 'http://api.klgwl.com'
        elif debug == 1:
            host = 'http://120.78.182.253:8181'
        else:
            host = ''
    elif buniss == API_REDBAG:
        if debug == 0:
            host = 'http://service.klgwl.com'
        elif debug == 1:
            host = 'http://120.78.182.253'
        else:
            host = ''
    
    return host

if __name__ == '__main__':
    pass