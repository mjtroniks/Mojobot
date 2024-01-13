import machine
from time import *
led = machine.Pin("LED", machine.Pin.OUT)
while True:
    led.on()
    sleep(0.5)
    led.off()
    sleep(0.5)
