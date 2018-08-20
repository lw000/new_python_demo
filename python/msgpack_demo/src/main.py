'''
Created on 2018年6月12日

@author: Administrator
'''

# import sys
# import time
# import json

import msgpack

if __name__ == '__main__':
    a = {'name':'yzy', 'age':26, 'gender':'male', 'location':'shenzhen','ext':[0,1,2,3,4,5,6,7,8,9]}
    in_msg = msgpack.packb(a)
    print(in_msg)
    un_msg = msgpack.unpackb(in_msg)
    print(un_msg)