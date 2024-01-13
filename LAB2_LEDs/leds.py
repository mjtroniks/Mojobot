# Complete project details at https://RandomNerdTutorials.com/raspberry-pi-pico-pwm-micropython/
from machine import Pin, PWM
from time import sleep
#LEDL        LEDR
#R GP7      R GP28
#B GP8      B GP27
#G GP9      G GP26
# Set up PWM Pin
led = Pin(28)
led_pwm = PWM(led)
duty_step = 255  # Step size for changing the duty cycle

while True:

        # Increase the duty cycle gradually
        for duty_cycle in range(0, 65536, duty_step):
            led_pwm.duty_u16(duty_cycle)
            sleep(0.005)

        # Decrease the duty cycle gradually
        for duty_cycle in range(65536, 0, -duty_step):
            led_pwm.duty_u16(duty_cycle)
            sleep(0.005)
