#*****************************
#* Developer: MJtronics
#* Date: 2024-01-15
#*****************************

# Description:
# This MicroPython script allows the user to interactively control the brightness of an LED using Pulse Width Modulation (PWM).
# The script prompts the user to input a value in the range of 0 to 255, which represents the desired brightness level.
# The input is then mapped to the PWM range (0 to 65535) and applied to the LED, creating a smooth brightness adjustment effect.

# Pin Configuration:
# LEDL (Left LED)
# - R: GP22
# - B: GP21
# - G: GP20

# LEDR (Right LED)
# - R: GP7
# - B: GP8
# - G: GP9

from machine import Pin, PWM

# Function to map user input (0-255) to PWM range (0-65535)
def map_user_input(user_input):
    # Ensure user_input is within the valid range
    user_input = max(0, min(255, user_input))
    # Map the value to the PWM range
    return int((user_input / 255) * 65535)

# Function to set LED brightness using PWM
def set_led_brightness(pwm, brightness):
    pwm.duty_u16(brightness)

# Define the LED pin for the Right LED (GP7)
frequency = 5000
led_pin_right = Pin(7)
led_pin_right.freq(frequency)
# Initialize PWM on the Right LED pin
led_pwm_right = PWM(led_pin_right)

while True:
    try:
        # Get user input from 0 to 255
        user_input = int(input("Enter a value (0-255): "))
        # Map user input to PWM range
        pwm_value = map_user_input(user_input)
        # Set Right LED brightness
        set_led_brightness(led_pwm_right, pwm_value)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
