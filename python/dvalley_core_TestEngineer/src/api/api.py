#!/usr/bin/env python
# -*- coding=utf-8 -*-

'''
Created on 2018年05月31日

@author: Administrator
'''

from api_login import LoginApi
from api_user import UserApi
from api_discuss import DiscussApi
from api_setting import SettingApi
from api_area import AreaApi
from api_social import SocialApi
from api_contact import ContactApi

from api_wallet import WalletApi

class TesterApi():
    def __init__(self, debug=1):
        self.__loginer = LoginApi(debug)
        
        self.__apiModules = []
        self.__apiModules.append(UserApi(debug))
        self.__apiModules.append(DiscussApi(debug))
        self.__apiModules.append(SettingApi(debug))
        self.__apiModules.append(AreaApi(debug))
        self.__apiModules.append(SocialApi(debug))
        self.__apiModules.append(WalletApi(debug))
        self.__apiModules.append(ContactApi(debug))
        
    def start(self):
        for _, v in enumerate(self.__apiModules):
            v.start()
                        
    def stop(self):
        for _, v in enumerate(self.__apiModules):
            v.stop()
    
    def login(self, account, pwd):
        ok = self.__loginer.login(account, pwd)
        return ok
    
    @property
    def account(self):
        return self.__loginer.account
    
    @account.setter
    def account(self, account):
        self.__loginer.account = account
        
    @property
    def pwd(self):
        return self.__loginer.pwd
     
    @pwd.setter
    def pwd(self, pwd):
        self.__loginer.pwd = pwd
        

                                        