'''
Created on 2017骞�12鏈�29鏃�

@author: Administrator
'''

import sys
import socket
import os
import time
import  getopt
from datetime import datetime
from datetime import date
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.schedulers.gevent import GeventScheduler
import threading

#=======================================================
# MQTT Initialize.--------------------------------------
try:
    import paho.mqtt.client as mqtt
    import paho.mqtt.publish as publish
    import paho.mqtt.subscribe as subscribe
    
except ImportError:
    print('MQTT client not find. Please install as follow:')
    print('git clone http://git.eclipse.org/gitroot/paho/org.eclipse.paho.mqtt.python.git')
    print('cd org.eclipse.paho.mqtt.python')
    print('sudo python setup.py install')

#======================================================

#RPi.GPIO 妯″潡浣跨敤鍩虹

channel_common_000 = '/common/000'
channel_liwei_000 = '/liwei/000'
channel_liwei_111 = '/liwei/111'
channel_heshanshan_000 = '/heshanshan/000'
channel_heshanshan_111 = '/heshanshan/111'

channel_lot_message = '/lot/message'

# broker = 'localhost'
broker = '120.78.182.253'

count = 0

def transmitMQTT(msg = 'this is a test message.'):
    global count
    msg = msg + str(count);
    count += 1
    
    publish.single(topic=channel_liwei_000, payload=msg, hostname = broker, client_id='tcp_client')
    publish.single(topic=channel_liwei_111, payload=msg, hostname = broker, client_id='tcp_client')
    publish.single(topic=channel_heshanshan_000, payload=msg, hostname = broker, client_id='tcp_client')
    publish.single(topic=channel_heshanshan_111, payload=msg, hostname = broker, client_id='tcp_client')
    
def on_connect(client, userdata, flags, rc):
    print('on_connect, rc: ' + str(rc))
    if rc == 0:
        client.publish(topic=channel_common_000, payload='i\'m python client')

def on_publish(client, obj, mid):
    print('on_publish, mid: ' + str(mid))

def on_subscribe(client, obj, mid, granted_qos):
    print('on_subscribe: ' + str(mid) + ' ' + str(granted_qos))

def on_log(client, obj, level, string):
#     print('on_log:' + string)
    pass

def on_message(client, obj, msg):
    if msg.topic == channel_liwei_000 or msg.topic == channel_liwei_111:
        curtime = datetime.now()
        strcurtime = curtime.strftime('%Y-%m-%d %H:%M:%S')
        print(strcurtime + ': ' + msg.topic + ' ' +
              str(msg.qos) + ' ' + str(msg.payload))
        on_exec(str(msg.payload))
    elif msg.topic == channel_common_000:
        curtime = datetime.now()
        strcurtime = curtime.strftime('%Y-%m-%d %H:%M:%S')
        print(strcurtime + ': ' + msg.topic + ' ' +
              str(msg.qos) + ' ' + str(msg.payload))
    elif msg.topic == channel_lot_message:
        curtime = datetime.now()
        strcurtime = curtime.strftime('%Y-%m-%d %H:%M:%S')
        print(strcurtime + ': ' + msg.topic + ' ' +
              str(msg.qos) + ' ' + str(msg.payload))
    else:
        pass

def on_exec(strcmd):
    print('on_exec:', strcmd)
  
if __name__ == '__main__':
    opts, _ = getopt.getopt(sys.argv[1:], 'ht:m:')
    s = ''
    m = ''
    for op, v in opts:
        if op == '-t':
            s = v
        elif op == '-m':
            m = v
            
    if s == 's':
        try:
            client = mqtt.Client(client_id='ws_client', transport='websockets')
#             client = mqtt.Client(client_id='tcp_client', transport='tcp')
            client.on_message = on_message
            client.on_connect = on_connect
            client.on_publish = on_publish
            client.on_subscribe = on_subscribe
            client.on_log = on_log
            
            client.connect(broker, port=9001)
            
            client.subscribe(topic=channel_common_000, qos=0)
            client.subscribe(topic=channel_liwei_000, qos=0)
            client.subscribe(topic=channel_liwei_111, qos=0)
            client.subscribe(topic=channel_lot_message, qos=0)
            
            client.loop_forever()
    
        except (KeyboardInterrupt, SystemExit):
            client.disconnect()
            
    elif s == 'p':
#         sched = BackgroundScheduler()
#         sched.add_job(transmitMQTT, 'interval', seconds=1, args=(m,))  #interval 闂撮殧璋冨害锛堟瘡闅斿涔呮墽琛岋級
#         sched.start()
#         try:
#             while True:
#                 time.sleep(10)
#         except (KeyboardInterrupt, SystemExit):
#             sched.shutdown()
 
        sched = GeventScheduler()
        sched.add_job(transmitMQTT, 'interval', seconds=1, args=(m,))
        g = sched.start()
    
        try:
            g.join()
        except (KeyboardInterrupt, SystemExit):
            pass