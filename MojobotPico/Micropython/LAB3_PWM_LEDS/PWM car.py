from machine import Pin, PWM
from time import sleep

# Initialize PWM pins for RGB LEDs
def init_pwm(pin):
    pwm = PWM(Pin(pin))
    pwm.freq(5000)
    return pwm

# Set up PWM for left and right RGB LEDs
pwm_red_left = init_pwm(22)
pwm_green_left = init_pwm(21)
pwm_blue_left = init_pwm(20)

pwm_red_right = init_pwm(7)
pwm_green_right = init_pwm(8)
pwm_blue_right = init_pwm(9)

def set_rgb(pwm_red, pwm_green, pwm_blue, red, green, blue):
    pwm_red.duty_u16(red)
    pwm_green.duty_u16(green)
    pwm_blue.duty_u16(blue)

def map_input(value):
    return int((max(0, min(255, value)) / 255) * 65535)

while True:
    # Set RGB values for both LEDs
    red_value = map_input(255)
    green_value = map_input(255)
    blue_value = map_input(255)

    set_rgb(pwm_red_left, pwm_green_left, pwm_blue_left, red_value, green_value, blue_value)
    set_rgb(pwm_red_right, pwm_green_right, pwm_blue_right, red_value, green_value, blue_value)
    sleep(2)
