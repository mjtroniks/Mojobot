"""
*****************************
* Developer: MJtronics
* Date: 2024-01-15
*****************************

Description:
This code demonstrates PWM (Pulse Width Modulation) on a Raspberry Pi Pico using MicroPython.
It gradually increases and decreases the duty cycle of an LED connected to pin GP28, creating
a smooth fading effect.

Pin Configuration:
# LEDL (Left LED)
- R: GP22
- B: GP21
- G: GP20

# LEDR (Right LED)
- R: GP28
- B: GP27
- G: GP26
"""

from machine import Pin, PWM
from time import sleep

# LED Pin Configuration
# LEDR (Right LED) is connected to GP28
led = Pin(22)
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
