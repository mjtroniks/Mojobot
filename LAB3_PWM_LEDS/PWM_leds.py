"""
*****************************
* Developer: MJtronics
* Date: 2024-01-15
*****************************

Description:
This code controls two sets of RGB LEDs using PWM signals on a microcontroller.
It gradually increases and decreases the duty cycle of both sets of RGB LEDs,
creating a smooth fading effect. One set is labeled "RGB Left" and the other "RGBR."

Pin Configuration:
- RGB Left:
  - Red: GP22
  - Green: GP20
  - Blue: GP21

- RGBR:
  - Red: GP7
  - Green: GP8
  - Blue: GP9

"""

import machine
from machine import Pin, PWM
from time import sleep

# Set up PWM Pins for RGB Left (GP22, GP20, GP21)
led_r = Pin(22)
led_g = Pin(20)
led_b = Pin(21)

pwm_r = PWM(led_r)
pwm_g = PWM(led_g)
pwm_b = PWM(led_b)

# Set PWM frequency for RGB Left
frequency = 5000
pwm_r.freq(frequency)
pwm_g.freq(frequency)
pwm_b.freq(frequency)

# Set up PWM Pins for RGBR (GP7, GP8, GP9)
led_r_r = Pin(7)
led_g_r = Pin(8)
led_b_r = Pin(9)

pwm_r_r = PWM(led_r_r)
pwm_g_r = PWM(led_g_r)
pwm_b_r = PWM(led_b_r)

# Set PWM frequency for RGBR
pwm_r_r.freq(frequency)
pwm_g_r.freq(frequency)
pwm_b_r.freq(frequency)

duty_step = 129  # Step size for changing the duty cycle

while True:
    # Increase the duty cycle gradually for both RGB sets
    for duty_cycle in range(0, 65536, duty_step):
        pwm_r.duty_u16(duty_cycle)
        pwm_g.duty_u16(duty_cycle)
        pwm_b.duty_u16(duty_cycle)
        pwm_r_r.duty_u16(duty_cycle)
        pwm_g_r.duty_u16(duty_cycle)
        pwm_b_r.duty_u16(duty_cycle)
        sleep(0.005)

    # Decrease the duty cycle gradually for both RGB sets
    for duty_cycle in range(65536, 0, -duty_step):
        pwm_r.duty_u16(duty_cycle)
        pwm_g.duty_u16(duty_cycle)
        pwm_b.duty_u16(duty_cycle)
        pwm_r_r.duty_u16(duty_cycle)
        pwm_g_r.duty_u16(duty_cycle)
        pwm_b_r.duty_u16(duty_cycle)
        sleep(0.005)
