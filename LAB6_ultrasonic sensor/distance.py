import machine
import utime

led = machine.Pin("LED", machine.Pin.OUT)
led.on()

# Ultrasonic sensor pins
trigger_pin = machine.Pin(14, machine.Pin.OUT)
echo_pin = machine.Pin(15, machine.Pin.IN)  # Corrected to IN

def get_distance():
    pulse_time = 0
    trigger_pin.off()
    utime.sleep_us(2)
    trigger_pin.on()
    utime.sleep_us(10)
    trigger_pin.off()

    while echo_pin.value() == 0:
        pass

    if echo_pin.value() == 1:
        start = utime.ticks_us()
        while echo_pin.value() == 1:
            pass
        finish = utime.ticks_us()
        pulse_time = finish - start

    # To calculate the distance we get the pulse_time and divide it by 2
    # the sound speed in the air (343.2 m/s), that It's equivalent to
    # 0.034320 cm/us

    distance = pulse_time * 0.034 / 2

    return round(distance)

while True:
    print("Measuring ")
    distance_cm = get_distance()
    utime.sleep_ms(100)  # Adjust sleep duration as needed
    print(distance_cm)

##########################
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

    # Calculate distance in centimeters
    distance_cm = pulse_width * 0.034 / 2

    return distance_cm

try:
    while True:
        distance = measure_distance()
        utime.sleep_ms(100)
        print("Distance:", distance, "cm")


except KeyboardInterrupt:
    print("Measurement stopped by user")
