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
    if current_left_sensor_state == 0 and prev_left_sensor_state == 1:
        print("Left sensor detected a line!")
        led_left.on()  # Turn on left LED
    elif current_left_sensor_state == 1 and prev_left_sensor_state == 0:
        led_left.off()  # Turn off left LED

    # Check for changes in right sensor state
    if current_right_sensor_state == 0 and prev_right_sensor_state == 1:
        print("Right sensor detected a line!")
        led_right.on()  # Turn on right LED
    elif current_right_sensor_state == 1 and prev_right_sensor_state == 0:
        led_right.off()  # Turn off right LED

    # Update previous sensor states
    prev_left_sensor_state = current_left_sensor_state
    prev_right_sensor_state = current_right_sensor_state

    utime.sleep_ms(100)  # Wait for a short duration before checking again
