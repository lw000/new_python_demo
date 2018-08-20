# -*- coding: UTF-8 -*-

'''
Created on 2018年6月1日

@author: Administrator
'''

import xlrd
import xlwt
import time
import datetime
import copy
from people import People
from concurrent.futures.thread import ThreadPoolExecutor

testerConfig = {}

def readExecl(f):
    xls = xlrd.open_workbook(f)
    sheets = xls.sheets()
    for sheet in sheets:
        print(sheet.row_values(0))
        print(sheet.row_values(1))
        testerConfig['host'] = sheet.row_values(0)
        testerConfig['host1'] = sheet.row_values(1)
        
def writeExecl(f, sheet):
    xls = xlwt.Workbook()
    sheet = xls.add_sheet(sheet)
    sheet.write(0, 0, 'www.baidu.com')
    sheet.write(0, 1, 'www.google.com')
    sheet.write(0, 2, 'www.sina.com')
    sheet.write(0, 3, 'www.alipay.com')
    
    sheet.write(1, 0, 'www.baidu.com')
    sheet.write(1, 1, 'www.google.com')
    sheet.write(1, 2, 'www.sina.com')
    sheet.write(1, 3, 'www.alipay.com')
    
    xls.save(f)
    
    print('write execl file [%s] ok.' % (f))
    
    return True

def readFile(f):
    block_size = 1024*10
    with open(f, 'rb') as f:
        while True:
            block = f.read(block_size)
            if block:
                yield block
            else:
                return
        
def hook(func):
    def wrapper():
        func()
        hook = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(hook)
    return wrapper

def hook_date(func):
    def wrapper(v):
        func(v)
        hook = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print('%s [%s]' % (hook, v))    
    return wrapper
 
@hook
def alan():
    print('alan speaking')
    
@hook_date
def tom(v):
    print('tom speaking: %s' % (v))
 

def test_func(a, b):
    print('%d, %d' % (a, b))
    return a + b
   
def fab(m):
    n, a, b = 0, 0, 1
    L = []
    while n < m:
        L.append(b)
        a, b = b, a + b
        n = n + 1
    return L

def fab_gen(m):
    n, a, b = 0, 0, 1
    while n < m:
        yield b
        a, b = b, a + b
        n = n + 1
               
if __name__ == '__main__':
    f = 'sample.xls'
    if writeExecl(f, 'sample'):
        readExecl(f)
    
    alan()
    tom('hello')
    
    v = {'a':100, 'b':200}
    print(v.items())
    print(v.keys())
    print(v.values())
    
    people = People()
    people.name = '李伟'
    people.age = 30
    people.sex = 1
    people.address = '广东省深圳市宝安区西乡芬达科技园对面雅居园11单元1202'
    people.birthday = '19840604'
    people.IDcardNo = '61015198406047512'
    print(people)
    
    people1 = people
    people1.name = '何珊珊'
    people1.age = 18
    people1.sex = 0
    people1.address = '广东省深圳市宝安区西乡芬达科技园对面雅居园11单元1202'
    people1.birthday = '19860526'
    people1.IDcardNo = '450332198605264124'
    print(people)
    print(people1)
    
    people2 = copy.deepcopy(people)
    people2.name = '李诗彤'
    people2.age = 5
    people2.sex = 0
    people2.address = '广东省深圳市宝安区西乡芬达科技园对面雅居园11单元1202'
    print(people)
    print(people2)
            
    executor = ThreadPoolExecutor(3)
    result = executor.map(test_func, [4, 7, 1], [4, 7, 1])
    for v in result:
        print(v)
                
    L = fab(10)
    for i, v in enumerate(L):
        print(v)
        
#     for i in range(len(L)-1):
#         print('%d/%d=%.30f' % (L[i], L[i+1], L[i]/L[i+1]))

    print('--------------------------------------------------------------------')

    for v in fab_gen(10):
        print(v)
        
    print('--------------------------------------------------------------------')
    
    t1 = time.time()
    for v in readFile('QQ图片20180522201815.jpg'):
#         print(v)
        pass
    t2 = time.time()
    print(t2-t1)
    
    print('--------------------------------------------------------------------')
    
    t1 = time.time()
    for v in readFile('bg_signup@2x.png'):
#         print(v)
        pass
    t2 = time.time()
    print(t2-t1)   
    