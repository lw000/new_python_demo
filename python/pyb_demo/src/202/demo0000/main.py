'''
Created on 2018��1��15��

@author: Administrator
'''

import network

#��v202���ó�APģʽ
ap_if = network.WLAN(network.AP_IF)
#����ӿ�
ap_if.active(True)
#����WIFI������:TPYBoard v202 ����:12345678
ap_if.config(essid='TPYBoard v202',password='12345678')