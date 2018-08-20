import dht
import machine
import network
import time
import ujson
from umqtt.simple import MQTTClient
from machine import Pin

#声明用到类库中的函数，并设置参数
d = dht.DHT11(machine.Pin(4))

led = Pin(2, Pin.OUT)

# Test reception e.g. with:
# mosquitto_sub -t foo_topic

count = 0

__channel_lot_message = '/lot/message'

#定义开发板连接无线网络的函数
def do_connect():
    #设置开发板的网#络模式
    wlan = network.WLAN(network.STA_IF)
    #打开网络连接
    wlan.active(True)
    #判断是否有网络连接
    if not wlan.isconnected():
        print('connecting to network...')
        #设置想要连接的无线名称和密码
        wlan.connect('12ZP', '12345678')
        #等待连接上无线网络
        while not wlan.isconnected():
            pass
        
    print('network config:', wlan.ifconfig())

do_connect()

def main(server='10.1.0.59'):
    c = MQTTClient('umqtt_client', server)
    c.connect()
    
    while 1:
        global count
        
        d.measure()#调用DHT类库中测量数据的函数
        
        temp_ = d.temperature()#读取measure()函数中的温度数据
        hum_ = d.humidity()#读取measure()函数中的湿度数据
        
        count += 1
        
        print('count: %d -- temp: %d -- hum:%d' % (count, temp_, hum_))
        
        led.value(not led.value())
        
        data = {'c':count, 't':temp_, 'h': hum_}
        s = ujson.dumps(data)
        c.publish(__channel_lot_message, s)
        
        time.sleep(5)
        
    c.disconnect()

if __name__ == '__main__':
    main()