#!/usr/bin/env python
# -*- coding=utf-8 -*-

'''
Created on 2018年05月31日

@author: Administrator
'''

import ctypes
import sys
import cProfile
import demjson
import time

PLATFORM = 'x64'

if PLATFORM == 'x64':
    sys.path.append(r"../x64")
else:
    sys.path.append(r"../x86")

if PLATFORM == 'x64':
    sys.path.append(r"../x64/python_ext.pyd")
    sys.path.append(r"../x64/calc.pyd")
    sys.path.append(r"../x64/rect_ext.pyd")
    export_c_func = ctypes.cdll.LoadLibrary('../x64/export_c_func.dll')
else:
    sys.path.append(r"../x86/python_ext.pyd")
    sys.path.append(r"../x86/calc_ext.pyd")
    sys.path.append(r"../x86/rect_ext.pyd")
    export_c_func = ctypes.cdll.LoadLibrary('../x86/export_c_func.dll')

import python_ext
import calc_ext
import rect_ext

# cdecl调用
# export_c_func = ctypes.CDLL(dllPath)

print('python_ext VERSION:', python_ext.VERSION)
print('python_ext VERSION_CODE:', python_ext.VERSION_CODE)
print('python_ext PLATFORM:', python_ext.PLATFORM)

def calc_ext_test():
    rect = calc_ext.Rect(10, 20)
    print('calc.rect.Area: ', calc_ext.Area(rect))
    print('calc.rect.Perimeter: ', calc_ext.Perimeter(rect))
    print('calc.rect.set_w_old: ', calc_ext.set_w(rect, 60))
    print('calc.rect.set_h_old: ', calc_ext.set_h(rect, 60))
    print('calc.rect.get_w: ', calc_ext.get_w(rect))
    print('calc.rect.get_h: ', calc_ext.get_h(rect))
    print('calc.rect.Area: ', calc_ext.Area(rect))
    print('calc.rect.Perimeter: ', calc_ext.Perimeter(rect))

    math = calc_ext.Math()
    print('calc.math.len: ', calc_ext.len(math, '0123456789'))
    print('calc.math.add: ', calc_ext.add(math, 1, 2))
    print('calc.math.sub: ', calc_ext.sub(math, 1, 2))
    print('calc.math.mul: ', calc_ext.mul(math, 1, 2))
    print('calc.math.fact: ', calc_ext.fact(math, 10))

def rect_ext_test():
    rc = rect_ext.Rect(10, 20)
    print('rect_ext.rect.Area: ', rect_ext.Area(rc))
    print('rect_ext.rect.Perimeter: ', rect_ext.Perimeter(rc))
    print('rect_ext.rect.setW: ', rect_ext.setW(rc, 60))
    print('rect_ext.rect.setH: ', rect_ext.setH(rc, 60))
    print('rect_ext.rect.getW: ', rect_ext.getW(rc))
    print('rect_ext.rect.getH: ', rect_ext.getH(rc))
    print('rect_ext.rect.Area: ', rect_ext.Area(rc))
    print('rect_ext.rect.Perimeter: ', rect_ext.Perimeter(rc))


def python_ext_test():
    print('python_ext.len1: ', python_ext.len1('0123456789'))
    print('python_ext.add1: ', python_ext.add1(1, 2))
    print('python_ext.sub1: ', python_ext.sub1(1, 2))
    print('python_ext.mul1: ', python_ext.mul1(1, 2))


if __name__ == '__main__':
#     CUR_PATH = os.path.dirname(__file__)
#     dllPath = os.path.join(CUR_PATH, 'export_c_func.dll')

#     rect_ext_test()
#     calc_ext_test()
#     python_ext_test()

    print('export_c_func.add: ', export_c_func.add(1,2))
    print('export_c_func.sub: ', export_c_func.sub(1,2))
    print('export_c_func.mul: ', export_c_func.mul(1,2))
