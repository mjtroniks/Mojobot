"""
*****************************
* Developer: MJtronics
* Date: 2024-01-15
*****************************

Description:
This code controls two RGB LEDs using PWM signals on a microcontroller.
It prompts the user for LED brightness input (0-255) and displays
alternating colors on the right and left RGB LEDs.

Expected Results:
- The RGB LEDs will display alternating green and red colors with the specified brightness.
- Each color will be displayed for a duration of 2 seconds, with a 2-second pause between actions.

"""

from machine import Pin, PWM
from time import sleep

frequency = 5000

def map_user_input(user_input):
    """
    Ensure user input is within the valid range (0-255) and map it to the PWM range.
    """
    user_input = max(0, min(255, user_input))
    return int((user_input / 255) * 65535)

def set_rgb_led(pwm_red, pwm_green, pwm_blue, r_value, g_value, b_value):
    """
    Set PWM values for the RGB LED to display a specific color.
    """
    pwm_red.duty_u16(r_value)
    pwm_green.duty_u16(g_value)
    pwm_blue.duty_u16(b_value)


def init_pins():
    """
    Initialize pins to avoid interference with PWM signals for motors.
    """
    Pin(10, mode=Pin.IN)
    Pin(11, mode=Pin.IN)


# Initialize pins
init_pins()

# Define the right RGB LED pins
led_red_right = Pin(7)
led_green_right = Pin(8)
led_blue_right = Pin(9)

# Set up PWM for the right RGB LED
pwm_red_right = PWM(led_red_right)
pwm_green_right = PWM(led_green_right)
pwm_blue_right = PWM(led_blue_right)
pwm_red_right.freq(frequency)
pwm_blue_right.freq(frequency)
pwm_green_right.freq(frequency)

# Define the left RGB LED pins
led_red_left = Pin(22)
led_green_left = Pin(21)
led_blue_left = Pin(20)

# Set up PWM for the left RGB LED
pwm_red_left = PWM(led_red_left)
pwm_green_left = PWM(led_green_left)
pwm_blue_left = PWM(led_blue_left)
pwm_red_left.freq(frequency)
pwm_blue_left.freq(frequency)
pwm_green_left.freq(frequency)


while True:

    rgbColor = map_user_input(255)
    set_rgb_led(pwm_red_right, pwm_green_right, pwm_blue_right, rgbColor,0 , 0)
    set_rgb_led(pwm_red_left, pwm_green_left, pwm_blue_left, 0, rgbColor, 0)
    sleep(2)

    set_rgb_led(pwm_red_right, pwm_green_right, pwm_blue_right, 0, rgbColor, 0)
    set_rgb_led(pwm_red_left, pwm_green_left, pwm_blue_left, rgbColor, 0, 0)
    sleep(2)

