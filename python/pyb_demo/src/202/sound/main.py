from machine import Pin
import time
from machine import Timer

p_out = Pin(4, Pin.OUT)

def printf_data():
    print('>>>>>>>>>>>>>>>> ', 2)

tim = Timer(-1)
tim.init(period=2000, mode=Timer.PERIODIC, callback=lambda t:print(2))

while True:
    v = p_out.value() # get value, 0 or 1
    if v == 0:
        print(v)
    time.sleep(0.1)