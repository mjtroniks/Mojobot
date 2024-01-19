"""
*****************************
* Developer: MJtronics
* Date: 2024-01-15
*****************************

Description:
This code reads data from two line following sensors and detects changes in their states.
It prints whether a line is detected or not based on the state changes of each sensor.

Pin Configuration:
- Left Sensor: GP2
- Right Sensor: GP3

"""

from machine import Pin
import utime

# Line following sensors
left_sensor_pin = Pin(2, Pin.IN)
right_sensor_pin = Pin(3, Pin.IN)

# Previous sensor states
prev_left_sensor_state = left_sensor_pin.value()
prev_right_sensor_state = right_sensor_pin.value()

while True:
    # Read current sensor states
    current_left_sensor_state = left_sensor_pin.value()
    current_right_sensor_state = right_sensor_pin.value()

    # Check for changes in sensor states
    if current_left_sensor_state != prev_left_sensor_state:
        print("Left Sensor state changed:", "Line Detected" if current_left_sensor_state else "No Line Detected")

    if current_right_sensor_state != prev_right_sensor_state:
        print("Right Sensor state changed:", "Line Detected" if current_right_sensor_state else "No Line Detected")

    # Update previous sensor states
    prev_left_sensor_state = current_left_sensor_state
    prev_right_sensor_state = current_right_sensor_state

    # Add a small delay to avoid excessive console output
    utime.sleep_ms(100)
