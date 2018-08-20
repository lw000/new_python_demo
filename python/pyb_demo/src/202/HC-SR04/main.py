from machine import Pin
import time
import network
import socket
import urllib

Trig = Pin(5, Pin.OUT)
Echo = Pin(4, Pin.IN)

led = Pin(2, Pin.OUT)

count = 0

def do_post_data(url):
    _, _, host, path = url.split('/', 3)
    addr = socket.getaddrinfo(host, 5000)[0][-1]    
    s = socket.socket()
    s.connect(addr)
    s.send(bytes('GET /%s HTTP/1.0\r\nHost:%s\r\n\r\n' % (path, host), 'utf8'))
    while True:
        data = s.recv(512)
        if data:
            reciver = str(data, 'utf8').upper()
            if reciver.find('YES') > -1:
                print('send data ok.')
        else:
            break
        
    s.close()

def do_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('12ZP', '12345678')
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())

do_connect()

while True:
    Trig.value(1)
    time.sleep_us(20)
    Trig.value(0)
    
    while Echo.value() == 0:
        Trig.value(1)
        time.sleep_us(20)
        Trig.value(0)

    if Echo.value() == 1:
        ts = time.ticks_us()
        while(Echo.value() == 1):
            pass

        te = time.ticks_us()
        tc = te - ts
# 测试距离=(高电平时间*声速(340M/S))/2。
        distance = (tc * 0.034) / 2
        print('Distance:', distance, 'cm')
        do_post_data('http://10.1.0.59/distance?distance=' + str(distance) + '')
        
        count += 1
        led.value(not led.value())
        
    time.sleep(1)
