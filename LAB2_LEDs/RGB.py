from machine import Pin, PWM
from time import sleep

# Define the RGB LED pins
red_pin = Pin(7)
green_pin = Pin(8)
blue_pin = Pin(9)

# Set up PWM for each color
red_pwm = PWM(red_pin)
green_pwm = PWM(green_pin)
blue_pwm = PWM(blue_pin)

# Set PWM frequency
frequency = 5000
red_pwm.freq(frequency)
green_pwm.freq(frequency)
blue_pwm.freq(frequency)

# Duty step size for changing the color
duty_step = 256

while True:
    # Increase the duty cycle gradually for red
    for duty_cycle in range(0, 65536, duty_step):
        red_pwm.duty_u16(duty_cycle)
        sleep(0.005)

    # Decrease the duty cycle gradually for red
    for duty_cycle in range(65535, 0, -duty_step):
        red_pwm.duty_u16(duty_cycle)
        sleep(0.005)

    # Increase the duty cycle gradually for green
    for duty_cycle in range(0, 65535, duty_step):
        green_pwm.duty_u16(duty_cycle)
        sleep(0.005)

    # Decrease the duty cycle gradually for green
    for duty_cycle in range(65535, 0, -duty_step):
        green_pwm.duty_u16(duty_cycle)
        sleep(0.005)

    # Increase the duty cycle gradually for blue
    for duty_cycle in range(0, 65535, duty_step):
        blue_pwm.duty_u16(duty_cycle)
        sleep(0.005)

    # Decrease the duty cycle gradually for blue
    for duty_cycle in range(65535, 0, -duty_step):
        blue_pwm.duty_u16(duty_cycle)
        sleep(0.005)
