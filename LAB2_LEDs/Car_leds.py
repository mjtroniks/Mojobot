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

def init_pins(): ## This fuctions avoids pin 10 and 11 being affected by the pwm in which case the motors move
    # Explicitly set pins 10 and 11 to INPUT mode
    Pin(10, mode=Pin.IN)
    Pin(11, mode=Pin.IN)

def main():
    # Initialize pins
    init_pins()

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
            brightness_percent = int(input("Enter led brightness (0-255): "))
            duration = 3  # Duration for each action

            rgb = map_user_input(brightness_percent)
            set_rgb_led(pwm_red_right, pwm_green_right, pwm_blue_right, 0, rgb, 0)  # Green color
            set_rgb_led(pwm_red_left, pwm_green_left, pwm_blue_left, 0, rgb, 0)  # Green color
            sleep(duration)

            turn_off_leds(pwm_red_right, pwm_green_right, pwm_blue_right)
            turn_off_leds(pwm_red_left, pwm_green_left, pwm_blue_left)
            sleep(3)  # Pause between actions

            rgb = map_user_input(brightness_percent)
            set_rgb_led(pwm_red_right, pwm_green_right, pwm_blue_right, 0, 0, rgb)  # Red color
            set_rgb_led(pwm_red_left, pwm_green_left, pwm_blue_left, 0, 0, rgb)  # Red color
            sleep(duration)

            turn_off_leds(pwm_red_right, pwm_green_right, pwm_blue_right)
            turn_off_leds(pwm_red_left, pwm_green_left, pwm_blue_left)
            sleep(3)  # Pause between actions

    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
