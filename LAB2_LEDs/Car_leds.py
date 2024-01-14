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


def main():
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

    # Set PWM frequency for both LEDs
    frequency = 5000
    pwm_red_right.freq(frequency)
    pwm_green_right.freq(frequency)
    pwm_blue_right.freq(frequency)
    pwm_red_left.freq(frequency)
    pwm_green_left.freq(frequency)
    pwm_blue_left.freq(frequency)

    try:
        while True:
            # Get user input for motor speed (0 to 100)
            speed_percent = int(input("Enter motor speed (0-100): "))
            duration = 3  # Duration for each action

            # Forward
            pwm_value = map_user_input(speed_percent)
            set_rgb_led(pwm_red_right, pwm_green_right, pwm_blue_right, 0, pwm_value, 0)  # Green color
            set_rgb_led(pwm_red_left, pwm_green_left, pwm_blue_left, 0, pwm_value, 0)  # Green color
            sleep(duration)

            # Stop
            turn_off_leds(pwm_red_right, pwm_green_right, pwm_blue_right)
            turn_off_leds(pwm_red_left, pwm_green_left, pwm_blue_left)
            sleep(3)  # Pause between actions

            # Backward
            pwm_value = map_user_input(speed_percent)
            set_rgb_led(pwm_red_right, pwm_green_right, pwm_blue_right, pwm_value, 0, 0)  # Red color
            set_rgb_led(pwm_red_left, pwm_green_left, pwm_blue_left, pwm_value, 0, 0)  # Red color
            sleep(duration)

            # Stop
            turn_off_leds(pwm_red_right, pwm_green_right, pwm_blue_right)
            turn_off_leds(pwm_red_left, pwm_green_left, pwm_blue_left)
            sleep(3)  # Pause between actions

    except ValueError:
        print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    main()
