from machine import Pin
import utime

# Line following sensors
left_sensor_pin = Pin(2, Pin.IN)
right_sensor_pin = Pin(3, Pin.IN)

# LEDs
led_left = Pin(7, Pin.OUT)
led_right = Pin(22, Pin.OUT)

# Previous sensor states
prev_left_sensor_state = left_sensor_pin.value()
prev_right_sensor_state = right_sensor_pin.value()

while True:
    # Read current sensor states
    current_left_sensor_state = left_sensor_pin.value()
    current_right_sensor_state = right_sensor_pin.value()

    # Check for changes in left sensor state
    if current_left_sensor_state == 1 and current_right_sensor_state == 0:
        print("Left sensor detected a line!")
        led_left.on()  # Turn on left LED
        led_right.off()
    elif current_left_sensor_state == 0 and current_right_sensor_state == 1:
        led_left.off()  # Turn on left LED
        led_right.on()
    # Check for changes in right sensor state
    elif current_left_sensor_state == 0 and current_right_sensor_state == 0:
        print("Right sensor detected a line!")
        led_right.on()  # Turn on right LED
    elif current_right_sensor_state == 1 and prev_right_sensor_state == 0:
        led_left.off()  # Turn on left LED
        led_right.off()
    elif current_right_sensor_state == 1 and prev_right_sensor_state == 1:
        led_left.on()  # Turn on left LED
        led_right.on()

