'''
Created on 2018年6月1日

@author: Administrator
'''

import xlrd
import xlwt
import datetime
import time

def readExecl(f):
    xls = xlrd.open_workbook(f)
    sheets = xls.sheets()
    for sheet in sheets:
        print(sheet.row_values(0))
        print(sheet.row_values(1))
        
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

def date(func):
    def wrapper():
        func()
        date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(date)
        
    return wrapper

def date1(func):
    def wrapper(v):
        func(v)
#         t = time.time()
#         date = datetime.datetime.fromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S')
        date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print('%s [%s]' % (date, v))
        
    return wrapper
 
@date
def alan():
    print('alan speaking')
    
@date1
def tom(v):
    print('tom speaking', v)
 
if __name__ == '__main__':
    f = 'sample.xls'
    if writeExecl(f, 'sample'):
        readExecl(f)
    
    alan()
    tom(1111)
    