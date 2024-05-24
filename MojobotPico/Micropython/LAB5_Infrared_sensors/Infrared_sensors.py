from machine import Pin, PWM
from time import sleep
import machine

# Sensor pins
left_sensor_pin = Pin(3, Pin.IN)
right_sensor_pin = Pin(2, Pin.IN)

# LED pins
left_led_pin = Pin(22, Pin.OUT)
right_led_pin = Pin(7, Pin.OUT)

blueR = Pin(9, Pin.OUT)
blueL = Pin(20, Pin.OUT)


def get_tracking():

    left = left_sensor_pin.value()
    right = right_sensor_pin.value()

    if left == 0 and right == 0:
        return 0
    elif left == 0 and right == 1:
        return 1
    elif left == 1 and right == 0:
        return 10
    elif left == 1 and right == 1:
        return 11


while True:
    tracking_state = get_tracking()


    if tracking_state == 0:
        print("Both sensor on a white reflective surface")
        left_led_pin.off()
        right_led_pin.off()  # Turn on right LED
        blueR.on()
        blueR.on()

    elif tracking_state == 1:
        print("Right triggered")

        left_led_pin.off()  # Turn on left LED
        right_led_pin.on()
        blueR.off()
        blueR.off()
    elif tracking_state == 10:
        print("Left triggered")
        left_led_pin.on()
        right_led_pin.off()  # Turn on right LED
        blueR.off()
        blueR.off()
    elif tracking_state == 11:
        print("Line detected")
        left_led_pin.on()  # Turn on left LED
        right_led_pin.on()
        blueR.off()
        blueR.off()