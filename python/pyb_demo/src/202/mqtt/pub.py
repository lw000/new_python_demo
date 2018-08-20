import dht
import machine
import network
import time
import ujson
from umqtt.simple import MQTTClient
from machine import Pin

#�����õ�����еĺ����������ò���
d = dht.DHT11(machine.Pin(4))

led = Pin(2, Pin.OUT)

# Test reception e.g. with:
# mosquitto_sub -t foo_topic

count = 0

__channel_lot_message = '/lot/message'

#���忪����������������ĺ���
def do_connect():
    #���ÿ��������#��ģʽ
    wlan = network.WLAN(network.STA_IF)
    #����������
    wlan.active(True)
    #�ж��Ƿ�����������
    if not wlan.isconnected():
        print('connecting to network...')
        #������Ҫ���ӵ��������ƺ�����
        wlan.connect('12ZP', '12345678')
        #�ȴ���������������
        while not wlan.isconnected():
            pass
        
    print('network config:', wlan.ifconfig())

do_connect()

def main(server='10.1.0.59'):
    c = MQTTClient('umqtt_client', server)
    c.connect()
    
    while 1:
        global count
        
        d.measure()#����DHT����в������ݵĺ���
        
        temp_ = d.temperature()#��ȡmeasure()�����е��¶�����
        hum_ = d.humidity()#��ȡmeasure()�����е�ʪ������
        
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