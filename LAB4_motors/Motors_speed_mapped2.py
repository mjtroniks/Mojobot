"""
*****************************
* Developer: MJtronics
* Date: 2024-01-15
*****************************

Description:
This code controls two motors using PWM signals on a microcontroller.
It defines functions for forward, backward, and stopping the motors.
The user is prompted for motor speed input (0-100), and the motors
demonstrate movement in both forward and backward directions with a 3-second duration.

Pin Configuration:
- Motor 1:
  - PWM: GP10
  - Direction: GP12

- Motor 2:
  - PWM: GP11
  - Direction: GP13

"""

from machine import Pin, PWM
from time import sleep
import machine

def map_speed_to_pwm(speed):
    """
    Ensure motor speed is within the valid range (0-100) and map it to the PWM range.
    """
    speed = max(0, min(100, speed))
    return int((speed / 100) * 65535)

def forward():
    """
    Move motors forward.
    """
    motor1_dir_pin.on()
    motor2_dir_pin.on()
    motor1_pwm.duty_u16(speed_pwm)
    motor2_pwm.duty_u16(speed_pwm)

def backward():
    """
    Move motors backward.
    """
    motor1_dir_pin.off()
    motor2_dir_pin.off()
    motor1_pwm.duty_u16(speed_pwm)
    motor2_pwm.duty_u16(speed_pwm)

def stop_motors():
    """
    Stop both motors.
    """
    motor1_pwm.duty_u16(0)
    motor2_pwm.duty_u16(0)

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

while True:
    try:
        # Get user input for motor speed (0 to 100)
        speed_percent = int(input("Enter motor speed (0-100): "))
        # Map speed to PWM range
        speed_pwm = map_speed_to_pwm(speed_percent)

        forward()
        sleep(3)
        stop_motors()
        sleep(3)
        backward()
        sleep(3)
        stop_motors()
        sleep(3)

    except ValueError:
        print("Invalid input. Please enter a valid number.")
