from machine import Pin
from machine import PWM
 
right_wheel_speed = None
left_wheel_speed = None

def gpio_set(pin,value):
    if value >= 1:
     Pin(pin, Pin.OUT).on()
    else:
     Pin(pin, Pin.OUT).off()

def motors(right_wheel_speed, left_wheel_speed):
   left_wheel_speed = ((left_wheel_speed - 0) * (65535 - 0)) / ((100 - 0) + 0)
   right_wheel_speed = ((right_wheel_speed - 0) * (65535 - 0)) / ((100 - 0) + 0)
   if left_wheel_speed > 0:
     # Motor1
     #
     gpio_set((12), True)
   if left_wheel_speed < 0:
     # Motor1
     #
     gpio_set((12), False)
   if right_wheel_speed > 0:
     gpio_set((13), True)
   if right_wheel_speed < 0:
     gpio_set((13), False)
   left_wheel_speed = left_wheel_speed if left_wheel_speed > 0 else left_wheel_speed * -1
   right_wheel_speed = right_wheel_speed if right_wheel_speed > 0 else right_wheel_speed * -1
   pwm10 = PWM(Pin(10))
   pwm10.freq(1000)
   pwm10.duty_u16(left_wheel_speed)
   pwm11 = PWM(Pin(11))
   pwm11.freq(1000)
   pwm11.duty_u16(right_wheel_speed)
 
 
while True:
   motors(30, 30)
 