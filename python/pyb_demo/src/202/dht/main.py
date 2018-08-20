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
        print('温度:', a, '°C')
        print('湿度:', b, '%')

tim = Timer(-1)  #新建一个虚拟定时器
tim.init(period=3000, mode=Timer.PERIODIC, callback=f)