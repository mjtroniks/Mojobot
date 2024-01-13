from machine import Pin, PWM
from time import sleep

# Define the LED pin
led_pin = Pin(8)
led_pwm = PWM(led_pin)

# Set PWM frequency
frequency = 5000
led_pwm.freq(frequency)

# Duty step size for changing the brightness
duty_step = 255

while True:
    # Increase the duty cycle gradually
    for duty_cycle in range(0, 65535, duty_step):
        led_pwm.duty_u16(duty_cycle)  # Scale duty cycle to 16-bit
        print(duty_cycle)
        sleep(0.005)

    # Decrease the duty cycle gradually
    for duty_cycle in range(65535, 0, -duty_step):
        led_pwm.duty_u16(duty_cycle)  # Scale duty cycle to 16-bit
        sleep(0.005)
