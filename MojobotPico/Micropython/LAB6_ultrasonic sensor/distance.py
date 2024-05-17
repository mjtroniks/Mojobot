"""
*****************************
* Developer: MJtronics
* Date: 2024-01-15
*****************************

Description:
This code measures the distance using an ultrasonic sensor and prints the result in centimeters.
The sensor cannot measure distances lower than 3cm.

Pin Configuration:
- Trigger Pin: GP14 (Output)
- Echo Pin: GP15 (Input)

"""

from machine import Pin, time_pulse_us
import utime

# Ultrasonic sensor pins
trigger_pin = Pin(14, Pin.OUT)
echo_pin = Pin(15, Pin.IN)

def measure_distance():
    # Trigger pulse to start measurement
    trigger_pin.off()
    utime.sleep_us(2)
    trigger_pin.on()
    utime.sleep_us(10)
    trigger_pin.off()

    # Measure the pulse width on the echo pin
    pulse_width = time_pulse_us(echo_pin, 1, 30000)  # 30ms timeout (max range)
    #speed of sound = 0.034 cm/us
    # Calculate distance in centimeters
    distance = pulse_width * 0.034 / 2 # division by 2 as we only need the time it takes to travel to the object

    return round(distance)


while True:

        distance_cm = measure_distance()
        print("Distance:", distance_cm, "cm")
        utime.sleep_ms(100)  # Adjust sleep duration as needed
