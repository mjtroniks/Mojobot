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
- Each color will be displayed for a duration of 3 seconds, with a 3-second pause between actions.

"""

from machine import Pin, PWM
from time import sleep

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

def turn_off_leds(pwm_red, pwm_green, pwm_blue):
    """
    Turn off all RGB LEDs by setting PWM values to 0.
    """
    pwm_red.duty_u16(0)
    pwm_green.duty_u16(0)
    pwm_blue.duty_u16(0)

def init_pins():
    """
    Initialize pins to avoid interference with PWM signals for motors.
    """
    Pin(10, mode=Pin.IN)
    Pin(11, mode=Pin.IN)

def main():
    # Initialize pins
    init_pins()

    # Define the right RGB LED pins
    led_red_right = Pin(28)
    led_green_right = Pin(26)
    led_blue_right = Pin(27)

    # Set up PWM for the right RGB LED
    pwm_red_right = PWM(led_red_right)
    pwm_green_right = PWM(led_green_right)
    pwm_blue_right = PWM(led_blue_right)

    # Define the left RGB LED pins
    led_red_left = Pin(7)
    led_green_left = Pin(9)
    led_blue_left = Pin(8)

    # Set up PWM for the left RGB LED
    pwm_red_left = PWM(led_red_left)
    pwm_green_left = PWM(led_green_left)
    pwm_blue_left = PWM(led_blue_left)

    try:
        while True:
            # Prompt user for LED brightness input
            brightness_percent = int(input("Enter LED brightness (0-255): "))
            duration = 3  # Duration for each color action

            # Display green color on both RGB LEDs
            rgb = map_user_input(brightness_percent)
            set_rgb_led(pwm_red_right, pwm_green_right, pwm_blue_right, 0, rgb, 0)
            set_rgb_led(pwm_red_left, pwm_green_left, pwm_blue_left, 0, rgb, 0)
            sleep(duration)

            # Turn off LEDs and pause
            turn_off_leds(pwm_red_right, pwm_green_right, pwm_blue_right)
            turn_off_leds(pwm_red_left, pwm_green_left, pwm_blue_left)
            sleep(3)  # Pause between actions

            # Display red color on both RGB LEDs
            rgb = map_user_input(brightness_percent)
            set_rgb_led(pwm_red_right, pwm_green_right, pwm_blue_right, 0, 0, rgb)
            set_rgb_led(pwm_red_left, pwm_green_left, pwm_blue_left, 0, 0, rgb)
            sleep(duration)

            # Turn off LEDs and pause
            turn_off_leds(pwm_red_right, pwm_green_right, pwm_blue_right)
            turn_off_leds(pwm_red_left, pwm_green_left, pwm_blue_left)
            sleep(3)  # Pause between actions

    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
