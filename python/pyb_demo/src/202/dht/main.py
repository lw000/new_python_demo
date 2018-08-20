from machine import Timer
import dht
import machine

p2 = machine.Pin(2, machine.Pin.OUT)
p2.value(1)

def f(t):
        d = dht.DHT11(machine.Pin(4))
        d.measure()
        a = d.temperature()
        b = d.humidity()
        p2.value(0)
        p2.value(1)
        print('�¶�:', a, '��C')
        print('ʪ��:', b, '%')

tim = Timer(-1)  #�½�һ�����ⶨʱ��
tim.init(period=3000, mode=Timer.PERIODIC, callback=f)