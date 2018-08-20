#!/usr/bin/env python
# -*- coding=utf-8 -*-

'''
Created on 2018年6月4日

@author: Administrator
'''

import json
import sqlite3
import configparser

class SqliteConfiure(object):
    
    def __init__(self):
        pass
    
    def open(self, f):
        self.__con = sqlite3.connect(f)
        return self.__con
    
    def close(self):
        self.__con.close()
    
    def createTable(self, sql):
        cu = self.__con.cursor()
        cu.execute(sql)
        cu.close()
        pass
    
    def readKey(self, key):
        pass
    
    def writeKey(self, key, value):
        pass

if __name__ == '__main__':
    configure = SqliteConfiure()
    configure.open('f.db')
    configure.createTable('create table catalog (id integer primary key, pid integer, name varchar(10) UNIQUE)')
    configure.close()