# -*- coding: UTF-8 -*-
'''
Created on 2018年6月8日

@author: Administrator
'''

import os
import xxtea

def xxtea_test_memory():
    s = 'xxtea is good'
#     key = os.urandom(16)
    key = b'1234567891234567'
    print('key:', key)
    
    enc = xxtea.encrypt(s, key)
    print(enc)
    
    dec = xxtea.decrypt(enc, key)
    print(dec)
    
    if s == dec.decode():
        print(True)
        
        
def xxtea_test_file():
    L = []
    with open('./鸿豚网络.txt', mode='r') as f:
        while True:
            buf = f.read(1024)
            if buf:
                L.append(buf)
            else:
                break
    print(L)
    return L
            
if __name__ == '__main__':
    
    l = os.listdir()
    print(l)
    
    xxtea_test_memory()
    
    xxtea_test_file()