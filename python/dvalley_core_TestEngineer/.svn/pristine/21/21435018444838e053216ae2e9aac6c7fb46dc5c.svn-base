#!/usr/bin/env python
# -*- coding=utf-8 -*-

'''
Created on 2018年05月31日

@author: Administrator
'''

import tester_config
from api_redbag_base import RedBagBaseApi

class WalletApi(RedBagBaseApi):
    def __init__(self, debug = 1):
        super(WalletApi, self).__init__(debug=debug)
            
    def start(self):
        self.__wallet_balance_check(method='/wallet/balance/check')
        self.__wallet_account_check(method='/wallet/account/check')
        self.__wallet_account_open(method='/wallet/account/open')
        self.__wallet_cashout_check(method='/wallet/cashout/check')
        self.__wallet_record_check(method='/wallet/cashout/check')
        
    def stop(self):
        pass
    
    #钱包功能开户
    def __wallet_account_open(self, method):
        params = dict(uid=tester_config.login_result_data['uid'])
        code, result = self.post(method=method, usetoken=True, params=params)
        if code == 200:
            print(result)
        else:
            print('[code: %d result:%s]' % (code, result))
            
    #查看账户详情
    def __wallet_account_check(self, method):
        params = dict(uid=tester_config.login_result_data['uid'], device_id='liwei')
        code, result = self.post(method=method, usetoken=True, params=params)
        if code == 200:
            print(result)
        else:
            print('[code: %d result:%s]' % (code, result))
            
    #钱包余额查询
    def __wallet_balance_check(self, method):
        params = dict(uid=tester_config.login_result_data['uid'])
        code, result = self.post(method=method, usetoken=True, params=params)
        if code == 200:
            print(result)
        else:
            print('[code: %d result:%s]' % (code, result))
    
    #查询自己的提现申请记录列表
    def __wallet_cashout_check(self, method):
        #type 查询的类型【0所有、1成功的、2未处理的，3被拒绝的，默认0】
        params = dict(uid=tester_config.login_result_data['uid'], type=0, lastid=0, limit=20)
        code, result = self.post(method=method, usetoken=True, params=params)
        if code == 200:
            print(result)
        else:
            print('[code: %d result:%s]' % (code, result))
    
    #查询资金动向记录
    def __wallet_record_check(self, method):
        #type 查询类型【0全部、1收入、2支出，默认0】
        #sub_type 0系统操作、1充值、2提现、3红包、4消费、5打赏、6系统奖励、7租人业务流水、8活动流水、9红包广场、10开店、11合伙人、12恐龙军推广红包
        params = dict(uid=tester_config.login_result_data['uid'], type=0, subtype=0, lastid=0, limit=20)
        code, result = self.post(method=method, usetoken=True, params=params)
        if code == 200:
            print(result)
        else:
            print('[code: %d result:%s]' % (code, result))
            
if __name__ == '__main__':
    from api_login import LoginApi
    
    debug = 0
    login = LoginApi(debug = debug)
    login.account = tester_config.account
    login.pwd = tester_config.pwd
    if login.login(tester_config.account, tester_config.pwd):
        tester = WalletApi(debug = debug)
        tester.start()
        tester.stop()
        
        
        
        
        
