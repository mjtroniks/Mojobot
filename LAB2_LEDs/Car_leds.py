from machine import Pin, PWM
from time import sleep

def map_user_input(user_input):
    # Ensure user_input is within the valid range
    user_input = max(0, min(255, user_input))
    # Map the value to the PWM range
    return int((user_input / 255) * 65535)

def set_rgb_led(pwm_red, pwm_green, pwm_blue, r_value, g_value, b_value):
    pwm_red.duty_u16(r_value)
    pwm_green.duty_u16(g_value)
    pwm_blue.duty_u16(b_value)

def turn_off_leds(pwm_red, pwm_green, pwm_blue):
    pwm_red.duty_u16(0)
    pwm_green.duty_u16(0)
    pwm_blue.duty_u16(0)

# Define the LED pins for the right RGB LED
led_red_right = Pin(28)
led_green_right = Pin(26)
led_blue_right = Pin(27)

# Set up PWM for the right RGB LED
pwm_red_right = PWM(led_red_right)
pwm_green_right = PWM(led_green_right)
pwm_blue_right = PWM(led_blue_right)

# Define the LED pins for the left RGB LED
led_red_left = Pin(7)
led_green_left = Pin(9)
led_blue_left = Pin(8)

# Set up PWM for the left RGB LED
pwm_red_left = PWM(led_red_left)
pwm_green_left = PWM(led_green_left)
pwm_blue_left = PWM(led_blue_left)

try:
    while True:
        # Get user input for both LEDs
        r_value_right = int(input("Enter the value for right LED (R) (0-255): "))
        g_value_right = int(input("Enter the value for right LED (G) (0-255): "))
        b_value_right = int(input("Enter the value for right LED (B) (0-255): "))
        r_value_left = int(input("Enter the value for left LED (R) (0-255): "))
        g_value_left = int(input("Enter the value for left LED (G) (0-255): "))
        b_value_left = int(input("Enter the value for left LED (B) (0-255): "))

        # Map user input to PWM range and set brightness for both LEDs
        set_rgb_led(pwm_red_right, pwm_green_right, pwm_blue_right, map_user_input(r_value_right), map_user_input(g_value_right), map_user_input(b_value_right))
        set_rgb_led(pwm_red_left, pwm_green_left, pwm_blue_left, map_user_input(r_value_left), map_user_input(g_value_left), map_user_input(b_value_left))

        sleep(2)

        # Turn off both LEDs
        turn_off_leds(pwm_red_right, pwm_green_right, pwm_blue_right)
        turn_off_leds(pwm_red_left, pwm_green_left, pwm_blue_left)

        sleep(2)

except ValueError:
    print("Invalid input. Please enter valid numbers.")
