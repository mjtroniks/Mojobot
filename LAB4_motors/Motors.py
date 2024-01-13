from machine import Pin, PWM
from time import sleep
import machine

# Motor 1
motor1_pwm_pin = Pin(10)
motor1_dir_pin = Pin(12, machine.Pin.OUT)
motor1_pwm = PWM(motor1_pwm_pin)

# Motor 2
motor2_pwm_pin = Pin(11)
motor2_dir_pin = Pin(13, machine.Pin.OUT)
motor2_pwm = PWM(motor2_pwm_pin)

# Set PWM frequency for motors
pwm_frequency = 1000
motor1_pwm.freq(pwm_frequency)
motor2_pwm.freq(pwm_frequency)
#The Raspberry Pi Pico has a 16-bit PWM resolution,
# meaning it supports duty cycle values from 0 to 65535. # max speed
# The value 32768 used in the code represents a 50% duty cycle,
# which corresponds to half of the maximum possible PWM value.
while True:
    # Forward for 3 seconds
    motor1_dir_pin.on()
    motor2_dir_pin.on()
    motor1_pwm.duty_u16(32768)  # Adjust duty cycle for forward speed
    motor2_pwm.duty_u16(32768)  # Adjust duty cycle for forward speed
    sleep(3)

    # Stop for 3 seconds
    motor1_pwm.duty_u16(0)
    motor2_pwm.duty_u16(0)
    sleep(3)

    # Backward for 3 seconds
    motor1_dir_pin.off()
    motor2_dir_pin.off()
    motor1_pwm.duty_u16(32768)  # Adjust duty cycle for backward speed
    motor2_pwm.duty_u16(32768)  # Adjust duty cycle for backward speed
    sleep(3)

    # Stop for 3 seconds
    motor1_pwm.duty_u16(0)
    motor2_pwm.duty_u16(0)
    sleep(3)
