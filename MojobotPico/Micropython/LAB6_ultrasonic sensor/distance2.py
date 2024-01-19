"""
*****************************
* Developer: MJtronics
* Date: 2024-01-15
*****************************

Description:
This code measures the distance using an ultrasonic sensor and prints the result in centimeters.
It uses the time_pulse_us function for accurate pulse width measurement and calculates distance
based on the duration of the pulse. The measurement stops if the user interrupts (e.g., keyboard interrupt).

Pin Configuration:
- Trigger Pin: GP14 (Output)
- Echo Pin: GP15 (Input)

"""

from machine import Pin, time_pulse_us
import utime

# Ultrasonic sensor pins
trigger_pin = Pin(14, Pin.OUT)
echo_pin = Pin(15, Pin.IN)

def get_distance():
    """
    Measures the distance using an ultrasonic sensor.

    Returns:
    - distance: Distance in centimeters.
    """
    # Trigger pulse to start measurement
    trigger_pin.off()
    utime.sleep_us(2)
    trigger_pin.on()
    utime.sleep_us(10)
    trigger_pin.off()

    # Measure the pulse width on the echo pin
    pulse_width = time_pulse_us(echo_pin, 1, 30000)  # 30ms timeout (max range)

    # Calculate distance in centimeters
    distance = (pulse_width / 2) / 29.1

    return distance

try:
    while True:
        # Measure distance and print result
        distance_cm = get_distance()
        utime.sleep_ms(100)  # To avoid measuring too frequently
        print("Distance:", distance_cm, "cm")

except KeyboardInterrupt:
    print("Measurement stopped by user")
