from machine import Pin, PWM


def map_user_input(user_input):
    # Ensure user_input is within the valid range
    user_input = max(0, min(255, user_input))
    # Map the value to the PWM range
    return int((user_input / 255) * 65535)

def set_led_brightness(pwm, brightness):
    pwm.duty_u16(brightness)

# Define the LED pin
led_pin = Pin(20)
led_pwm = PWM(led_pin)

while True:
    try:
        # Get user input from 0 to 255
        user_input = int(input("Enter a value (0-255): "))
        # Map user input to PWM range
        pwm_value = map_user_input(user_input)
        # Set LED brightness
        set_led_brightness(led_pwm, pwm_value)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
