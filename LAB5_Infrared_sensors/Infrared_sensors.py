from machine import Pin
import utime

# Line following sensors
sensor1_pin = Pin(2, Pin.IN)
sensor2_pin = Pin(3, Pin.IN)

# Previous sensor states
prev_sensor1_state = sensor1_pin.value()
prev_sensor2_state = sensor2_pin.value()

while True:
    # Read current sensor states
    current_sensor1_state = sensor1_pin.value()
    current_sensor2_state = sensor2_pin.value()

    # Check for changes in sensor states
    if current_sensor1_state != prev_sensor1_state:
        print("Sensor 1 state changed:", "Line Detected" if current_sensor1_state else "No Line Detected")

    if current_sensor2_state != prev_sensor2_state:
        print("Sensor 2 state changed:", "Line Detected" if current_sensor2_state else "No Line Detected")

    # Update previous sensor states
    prev_sensor1_state = current_sensor1_state
    prev_sensor2_state = current_sensor2_state

    # Add a small delay to avoid excessive console output
    utime.sleep_ms(100)
