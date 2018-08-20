import dht
import machine
import network
from machine import Pin
from machine import Timer
import socket
import urllib
import time

#�����õ�����⣬������dht�����

#�����õ�����еĺ����������ò���
d = dht.DHT11(machine.Pin(4))

led = Pin(2, Pin.OUT)

count=0

#���������ϴ��ĺ���
def http_get(url):
        _, _, host, path = url.split('/', 3)#�ָ�����Ĳ���
        addr = socket.getaddrinfo(host, 5000)[0][-1]#�Ѵ������Ĳ�������ɷ��ϸ�ʽ�ĵ�ַ
        s = socket.socket()
        s.connect(addr)#���ӵ�ַ
        s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))#�����ӵĵ�ַ��������
        while True:#��ʼ���ݷ���
                data = s.recv(50)
                if data:#����δ������ɣ���������
                        recive=str(data, 'utf8').upper()
                        #print(str(data, 'utf8'), end='')
                        if(recive.find('YES')>-1):
                            print('Send Data OK')
                else:#���ݷ�����ɣ��˳�while
                        break
        s.close()#�ر���������
        
#���忪����������������ĺ���
def do_connect():
        wlan = network.WLAN(network.STA_IF)#���ÿ��������#��ģʽ
        wlan.active(True)#����������
        if not wlan.isconnected():#�ж��Ƿ�����������
                print('connecting to network...')
                wlan.connect('12ZP', '12345678')#������Ҫ���ӵ��������ƺ�����
                while not wlan.isconnected():#�ȴ���������������
                        pass
        print('network config:', wlan.ifconfig())



def do_f(t):
    global count
    d.measure()#����DHT����в������ݵĺ���
    temp_=str(d.temperature())#��ȡmeasure()�����е��¶�����
    hum_=str(d.humidity())#��ȡmeasure()�����е�ʪ������
    count+=1#��������+1
    print('eg:',temp_,'-',hum_)
    led.value(not led.value())
    http_get('http://10.1.0.59/dht?c=' + str(count) + '&t=' + temp_ + '&h=' + hum_ + '')
    #���������ϴ������������²����õ������ݽ����ϴ�
    print('Count:',count)

#����һ�ο�����������������ĺ���
do_connect()

tm = Timer(-1)
tm.init(period=2000, mode=Timer.PERIODIC, callback=do_f)

# while True:#��ʼ��������Ĵ�ѭ��
#         d.measure()#����DHT����в������ݵĺ���
#         temp_=str(d.temperature())#��ȡmeasure()�����е��¶�����
#         hum_=str(d.humidity())#��ȡmeasure()�����е�ʪ������
#         count+=1#��������+1
#         print('eg:',temp_,'-',hum_)
#         led.value(not led.value())
#         http_get('http://10.1.0.59/dht?c=' + str(count) + '&t=' + temp_ + '&h=' + hum_ + '')
#         #���������ϴ������������²����õ������ݽ����ϴ�
#         print('Count:',count)
#         time.sleep(2)