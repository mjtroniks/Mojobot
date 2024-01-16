"""
*****************************
* Developer: MJtronics
* Date: 2024-01-15
*****************************

Description:
This code controls RGB LEDs and two motors. It receives user input for motor speed, maps it to PWM range,
and performs forward and backward movements with corresponding LED colors. The actions are repeated in a loop.

Pin Configuration:
- RGB LEDs:
  * Right LED: Red(GP22), Green(GP20), Blue(GP21)
  * Left LED: Red(GP7), Green(GP9), Blue(GP8)
- Motors:
  * Motor 1: PWM Pin(GP10), Direction Pin(GP12)
  * Motor 2: PWM Pin(GP11), Direction Pin(GP13)

"""

import machine
from machine import Pin, PWM
from time import sleep

#######################Leds###############################
# Define the RGB LED pins for the right RGB LED
led_red_right = Pin(22)
led_green_right = Pin(20)
led_blue_right = Pin(21)

# Set up PWM for the right RGB LED
pwm_red_right = PWM(led_red_right)
pwm_green_right = PWM(led_green_right)
pwm_blue_right = PWM(led_blue_right)

# Define the RGB LED pins for the left RGB LED
led_red_left = Pin(7)
led_green_left = Pin(9)
led_blue_left = Pin(8)

# Set up PWM for the left RGB LED
pwm_red_left = PWM(led_red_left)
pwm_green_left = PWM(led_green_left)
pwm_blue_left = PWM(led_blue_left)

# Set PWM frequency for both LEDs
frequency = 5000
pwm_red_right.freq(frequency)
pwm_green_right.freq(frequency)
pwm_blue_right.freq(frequency)
pwm_red_left.freq(frequency)
pwm_green_left.freq(frequency)
pwm_blue_left.freq(frequency)

###################Motors#######################################
""""" Motor 1  """""
motor1_pwm_pin = Pin(10)
motor1_dir_pin = Pin(12, machine.Pin.OUT)
motor1_pwm = PWM(motor1_pwm_pin, freq=1000)  # Explicitly set frequency for isolation

""""" Motor 2  """""
motor2_pwm_pin = Pin(11)
motor2_dir_pin = Pin(13, machine.Pin.OUT)
motor2_pwm = PWM(motor2_pwm_pin, freq=1000)  # Explicitly set frequency for isolation

def map_user_input(user_input):
    """
    Maps user input to PWM range.

    Args:
    - user_input: User input value (0 to 255).

    Returns:
    - int: Mapped value in the PWM range (0 to 65535).
    """
    # Ensure user_input is within the valid range
    user_input = max(0, min(255, user_input))
    # Map the value to the PWM range
    return int((user_input / 255) * 65535)

def set_rgb_led(pwm_red, pwm_green, pwm_blue, r_value, g_value, b_value):
    """
    Sets RGB LED colors using PWM values.

    Args:
    - pwm_red: PWM object for the red LED.
    - pwm_green: PWM object for the green LED.
    - pwm_blue: PWM object for the blue LED.
    - r_value: PWM value for the red color.
    - g_value: PWM value for the green color.
    - b_value: PWM value for the blue color.
    """
    pwm_red.duty_u16(r_value)
    pwm_green.duty_u16(g_value)
    pwm_blue.duty_u16(b_value)

def turn_off_leds(pwm_red, pwm_green, pwm_blue):
    """
    Turns off RGB LEDs.

    Args:
    - pwm_red: PWM object for the red LED.
    - pwm_green: PWM object for the green LED.
    - pwm_blue: PWM object for the blue LED.
    """
    pwm_red.duty_u16(0)
    pwm_green.duty_u16(0)
    pwm_blue.duty_u16(0)

def map_speed_to_pwm(speed):
    """
    Maps speed percentage to PWM range.

    Args:
    - speed: Motor speed percentage (0 to 100).

    Returns:
    - int: Mapped value in the PWM range (0 to 65535).
    """
    # Ensure speed is within the valid range
    speed = max(0, min(100, speed))
    # Map the speed to the PWM range
    return int((speed / 100) * 65535)

def forward():
    """
    Moves both motors forward.
    """
    motor1_dir_pin.on()
    motor2_dir_pin.on()
    motor1_pwm.duty_u16(speed_pwm)
    motor2_pwm.duty_u16(speed_pwm)

def backward():
    """
    Moves both motors backward.
    """
    motor1_dir_pin.off()
    motor2_dir_pin.off()
    motor1_pwm.duty_u16(speed_pwm)
    motor2_pwm.duty_u16(speed_pwm)

def stop_motors():
    """
    Stops both motors.
    """
    motor1_pwm.duty_u16(0)
    motor2_pwm.duty_u16(0)

while True:
    try:
        # Get user input for motor speed (0 to 100)
        speed_percent = 40
        # Map speed to PWM range
        speed_pwm = map_speed_to_pwm(speed_percent)
        print(speed_pwm)

        # Forward
        pwm_value = map_user_input(255)
        set_rgb_led(pwm_red_right, pwm_green_right, pwm_blue_right, 0, pwm_value, 0)  # Green color
        set_rgb_led(pwm_red_left, pwm_green_left, pwm_blue_left, 0, pwm_value, 0)  # Green color
        forward()
        sleep(3)

        # Stop
        turn_off_leds(pwm_red_right, pwm_green_right, pwm_blue_right)
        turn_off_leds(pwm_red_left, pwm_green_left, pwm_blue_left)
        stop_motors()
        sleep(3)

        # Backward
        set_rgb_led(pwm_red_right, pwm_green_right, pwm_blue_right, pwm_value , 0, 0)  # Red color
        set_rgb_led(pwm_red_left, pwm_green_left, pwm_blue_left, pwm_value, 0, 0)  # Red color
        backward()
        sleep(3)

        # Stop
        turn_off_leds(pwm_red_right, pwm_green_right, pwm_blue_right)
        turn_off_leds(pwm_red_left, pwm_green_left, pwm_blue_left)
        stop_motors()
        sleep(3)

    except ValueError:
        print("Invalid input. Please enter a valid number.")
