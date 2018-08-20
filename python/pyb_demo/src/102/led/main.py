'''
Created on 2018Äê1ÔÂ12ÈÕ

@author: Administrator
'''

import pyb

led1 = pyb.Pin("Y1",pyb.Pin.OUT_PP)
led2 = pyb.Pin("Y2",pyb.Pin.OUT_PP)
led3 = pyb.Pin("Y3",pyb.Pin.OUT_PP)

ls = [led1, led2, led3]

n = 0

while True:
    led1.value(1)
    led2.value(1)
    led3.value(1)