"""
Test Program for Mojobot
Author: MJtroniks
Website: www.mjtroniks.com
GitHub: https://github.com/mjtroniks/Mojobot

This program is designed to verify that all hardware components of the Mojobot are functioning as expected.
It performs the following tests:

1. **Red LEDs and Ultrasonic Sensor**:
   - Measures distance using the ultrasonic sensor.
   - Adjusts the brightness of the red LEDs based on the distance measured.
   - The red LEDs are at maximum brightness when the distance is 100 cm or more, and at minimum brightness when the distance is 10 cm or less.

2. **Blue LEDs and Infrared Sensors**:
   - Checks the infrared sensors to detect a black surface.
   - Turns on the corresponding blue LED if a black surface is detected by the left or right infrared sensor.

3. **Motors and Green LEDs**:
   - Tests the left motor and green LED based on the distance measured.
   - The left motor and green LED's speed and brightness vary from minimum (at 2 cm) to maximum (at 50 cm).
   - Repeats the same test for the right motor and green LED after turning off the left motor and LED.

This program can be implemented to verify that all hardware is working as expected.
"""

import machine
import utime
from machine import Pin, time_pulse_us
import utime

# Turn on the onboard LED to indicate the program has started
onboard_led = machine.Pin(25, machine.Pin.OUT)
onboard_led.value(1)

# Pin configuration
trigger_pin = Pin(14, Pin.OUT)
echo_pin = Pin(15, Pin.IN)

led_left_red = machine.PWM(machine.Pin(22))
led_left_green = machine.PWM(machine.Pin(20))
led_left_blue = machine.PWM(machine.Pin(21))

led_right_red = machine.PWM(machine.Pin(7))
led_right_green = machine.PWM(machine.Pin(9))
led_right_blue = machine.PWM(machine.Pin(8))

infrared_left = machine.Pin(3, machine.Pin.IN)
infrared_right = machine.Pin(2, machine.Pin.IN)

motor1_pwm = machine.PWM(machine.Pin(10))
motor1_dir = machine.Pin(12, machine.Pin.OUT)
motor2_pwm = machine.PWM(machine.Pin(11))
motor2_dir = machine.Pin(13, machine.Pin.OUT)

# Set PWM frequency for LEDs and motors
led_left_red.freq(1000)
led_left_green.freq(1000)
led_left_blue.freq(1000)
led_right_red.freq(1000)
led_right_green.freq(1000)
led_right_blue.freq(1000)

motor1_pwm.freq(1000)
motor2_pwm.freq(1000)

# Function to measure distance using ultrasonic sensor
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
    distance = pulse_width * 0.034 / 2  # Speed of sound = 0.034 cm/us
    return distance

# Function to control LED brightness based on distance
def control_red_leds_by_distance():
    #print("Controlling Red LEDs by Distance")
    led_left_red.duty_u16(0)
    led_right_red.duty_u16(0)
    led_left_blue.duty_u16(0)
    led_right_blue.duty_u16(0)
    led_left_green.duty_u16(0)
    led_right_green.duty_u16(0)
    motor1_pwm.duty_u16(0)
    motor2_pwm.duty_u16(0)
    for _ in range(500):
        distance = measure_distance()
        #print("Distance:", distance)
        if distance <= 5:
            pwm_value = 0
        elif distance >= 40:
            pwm_value = 65535
        else:
            pwm_value = int((distance / 30) * 65535)

        led_left_red.duty_u16(pwm_value)
        led_right_red.duty_u16(pwm_value)
        utime.sleep(0.01)
    utime.sleep(5)
    led_left_red.duty_u16(0)
    led_right_red.duty_u16(0)

# Function to control blue LEDs based on infrared sensors
def control_blue_leds_by_infrared():
    #print("Controlling Blue LEDs by Infrared Sensors")

    for _ in range(500):
        left_value = infrared_left.value()
        right_value = infrared_right.value()
        #print("Infrared Left:", left_value, "Infrared Right:", right_value)

        if left_value == 1:
            led_left_blue.duty_u16(65535)
        else:
            led_left_blue.duty_u16(0)

        if right_value == 1:
            led_right_blue.duty_u16(65535)
        else:
            led_right_blue.duty_u16(0)

        utime.sleep(0.01)
    utime.sleep(5)
    led_left_blue.duty_u16(0)
    led_right_blue.duty_u16(0)

# Function to control motors and green LEDs based on distance
def control_motors_and_green_leds():
    #print("Controlling Motors and Green LEDs")

    # Function to map distance to PWM value
    def map_distance_to_pwm(distance):
        if distance <= 2:
            return 0
        elif distance >= 50:
            return 65535
        else:
            return int(((distance - 2) / 38) * 65535)

    # Test left motor and left green LED
    motor1_dir.high()
    motor2_pwm.duty_u16(0)  # Ensure right motor is off
    for _ in range(500):
        distance = measure_distance()
        #print("Distance (Left Motor):", distance)
        pwm_value = map_distance_to_pwm(distance)

        motor1_pwm.duty_u16(pwm_value)
        led_left_green.duty_u16(pwm_value)

        utime.sleep(0.01)
    motor1_pwm.duty_u16(0)
    led_left_green.duty_u16(0)
    utime.sleep(5)

    # Test right motor and right green LED
    motor2_dir.high()
    motor1_pwm.duty_u16(0)  # Ensure left motor is off
    for _ in range(500):
        distance = measure_distance()
        #print("Distance (Right Motor):", distance)
        pwm_value = map_distance_to_pwm(distance)

        motor2_pwm.duty_u16(pwm_value)
        led_right_green.duty_u16(pwm_value)

        utime.sleep(0.01)
    motor2_pwm.duty_u16(0)
    led_right_green.duty_u16(0)
    utime.sleep(5)
    led_left_green.duty_u16(0)
    led_right_green.duty_u16(0)

# Test sequence
def test_robot():

    control_red_leds_by_distance()
    control_blue_leds_by_infrared()
    control_motors_and_green_leds()

# Run the test
while True:
    test_robot()
