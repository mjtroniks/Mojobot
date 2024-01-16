"""
*****************************
* Developer: MJtronics
* Date: 2024-01-15
*****************************

Description:
This code controls RGB LEDs, two motors, an ultrasonic sensor, and infrared sensors. It receives distance
and infrared sensor measurements and adjusts the motor and LED actions based on the measured distance
and sensor states. The actions are repeated in a loop.

- If the distance is greater than 40 cm, the robot checks the infrared sensors:
- If the right sensor is active and the left sensor is inactive, it displays a green color on the right LED, turns off the left LED, and stops the motors.
- If the left sensor is active and the right sensor is inactive, it displays a green color on the left LED, turns off the right LED, and stops the motors.
- If both sensors are inactive, it turns off both LEDs and stops the motors.
- If both sensors are active, it turns off both LEDs and stops the motors.

- If the distance is between 5 cm and 20 cm, the robot moves forward with green color on both LEDs.

- If the distance is between 20 cm and 40 cm, the robot moves backward with red color on both LEDs.


Pin Configuration:
- Ultrasonic Sensor:
  * Trigger Pin(GP14), Echo Pin(GP15)
- RGB LEDs:
  * Right LED: Red(GP22), Green(GP20), Blue(GP21)
  * Left LED: Red(GP7), Green(GP9), Blue(GP8)
- Motors:
  * Motor 1: PWM Pin(GP10), Direction Pin(GP12)
  * Motor 2: PWM Pin(GP11), Direction Pin(GP13)
- Infrared Sensors:
  * Left Infrared Sensor: GP2
  * Right Infrared Sensor: GP3

"""

import machine
from machine import Pin, PWM, time_pulse_us
import utime

################## Ultrasonic ##############################
# Ultrasonic sensor pins
trigger_pin = Pin(14, Pin.OUT)
echo_pin = Pin(15, Pin.IN)

####################### LEDs ###############################
# Define the RGB LED pins for the right RGB LED
led_red_right = Pin(22)
led_green_right = Pin(20)
led_blue_right = Pin(21)

# Set up PWM for the right RGB LED
pwm_red_right = PWM(led_red_right)
pwm_green_right = PWM(led_green_right)
pwm_blue_right = PWM(led_blue_right)

# Define the RGB LED pins for the left RGB LED
led_red_left = Pin(7)
led_green_left = Pin(9)
led_blue_left = Pin(8)

# Set up PWM for the left RGB LED
pwm_red_left = PWM(led_red_left)
pwm_green_left = PWM(led_green_left)
pwm_blue_left = PWM(led_blue_left)

# Set PWM frequency for both LEDs
frequency = 5000
pwm_red_right.freq(frequency)
pwm_green_right.freq(frequency)
pwm_blue_right.freq(frequency)
pwm_red_left.freq(frequency)
pwm_green_left.freq(frequency)
pwm_blue_left.freq(frequency)

################### Motors #################################
# Motor 1
motor1_pwm_pin = Pin(10)
motor1_dir_pin = Pin(12, machine.Pin.OUT)
motor1_pwm = PWM(motor1_pwm_pin, freq=1000)  # Explicitly set frequency for isolation

# Motor 2
motor2_pwm_pin = Pin(11)
motor2_dir_pin = Pin(13, machine.Pin.OUT)
motor2_pwm = PWM(motor2_pwm_pin, freq=1000)  # Explicitly set frequency for isolation

################## Infrared #############################
# Line following sensors
infrared_left_pin = Pin(2, Pin.IN)  # left IR
infrared_right_pin = Pin(3, Pin.IN)  # right IR

# Previous sensor states
prev_infrared_left_state = infrared_left_pin.value()
prev_infrared_right_state = infrared_right_pin.value()

################# Functions ##############################
def map_user_input(user_input):
    """
    Maps user input to PWM range.

    Args:
    - user_input: User input value (0 to 255).

    Returns:
    - int: Mapped value in the PWM range (0 to 65535).
    """
    # Ensure user_input is within the valid range
    user_input = max(0, min(255, user_input))
    # Map the value to the PWM range
    return int((user_input / 255) * 65535)

def set_rgb_led(pwm_red, pwm_green, pwm_blue, r_value, g_value, b_value):
    """
    Sets RGB LED colors using PWM values.

    Args:
    - pwm_red: PWM object for the red LED.
    - pwm_green: PWM object for the green LED.
    - pwm_blue: PWM object for the blue LED.
    - r_value: PWM value for the red color.
    - g_value: PWM value for the green color.
    - b_value: PWM value for the blue color.
    """
    pwm_red.duty_u16(r_value)
    pwm_green.duty_u16(g_value)
    pwm_blue.duty_u16(b_value)

def turn_off_leds(pwm_red, pwm_green, pwm_blue):
    """
    Turns off RGB LEDs.

    Args:
    - pwm_red: PWM object for the red LED.
    - pwm_green: PWM object for the green LED.
    - pwm_blue: PWM object for the blue LED.
    """
    pwm_red.duty_u16(0)
    pwm_green.duty_u16(0)
    pwm_blue.duty_u16(0)

def map_speed_to_pwm(speed):
    """
    Maps speed percentage to PWM range.

    Args:
    - speed: Motor speed percentage (0 to 100).

    Returns:
    - int: Mapped value in the PWM range (0 to 65535).
    """
    # Ensure speed is within the valid range
    speed = max(0, min(100, speed))
    # Map the speed to the PWM range
    return int((speed / 100) * 65535)

def forward():
    """
    Moves both motors forward.
    """
    motor1_dir_pin.on()
    motor2_dir_pin.on()
    motor1_pwm.duty_u16(speed_pwm)
    motor2_pwm.duty_u16(speed_pwm)

def backward():
    """
    Moves both motors backward.
    """
    motor1_dir_pin.off()
    motor2_dir_pin.off()
    motor1_pwm.duty_u16(speed_pwm)
    motor2_pwm.duty_u16(speed_pwm)

def stop_motors():
    """
    Stops both motors.
    """
    motor1_pwm.duty_u16(0)
    motor2_pwm.duty_u16(0)

def get_distance():
    """
    Measures the distance using an ultrasonic sensor.

    Returns:
    - int: The distance in centimeters.
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

    return round(distance)

# Main Program
while True:
    try:
        distance_cm = get_distance()
        utime.sleep_ms(100)  # to avoid measuring too frequently
        # Get user input for motor speed (0 to 100)
        speed_percent = 40
        # Map speed to PWM range
        speed_pwm = map_speed_to_pwm(speed_percent)
        print(distance_cm)
        # Read current sensor states
        current_infrared_left_state = infrared_left_pin.value()  # left infrared sensor
        current_infrared_right_state = infrared_right_pin.value()  # right infrared sensor
        print("Infrared left " + str(current_infrared_left_state) + "  Infrared right " + str(
            current_infrared_right_state))

        if distance_cm > 40:
            if current_infrared_right_state == 1 and current_infrared_left_state == 0:
                pwm_valueR = map_user_input(17)
                pwm_valueG = map_user_input(236)
                pwm_valueB = map_user_input(229)
                set_rgb_led(pwm_red_right, pwm_green_right, pwm_blue_right, pwm_valueR, pwm_valueG,
                            pwm_valueB)  # Green color
                set_rgb_led(pwm_red_left, pwm_green_left, pwm_blue_left, 0, 0, 0)  # Green color
                stop_motors()
            if current_infrared_left_state == 1 and current_infrared_right_state == 0:
                pwm_valueR = map_user_input(17)
                pwm_valueG = map_user_input(236)
                pwm_valueB = map_user_input(229)
                set_rgb_led(pwm_red_right, pwm_green_right, pwm_blue_right, 0, 0, 0
                            )  # Green color
                set_rgb_led(pwm_red_left, pwm_green_left, pwm_blue_left, pwm_valueR, pwm_valueG, pwm_valueB)  # Green color
                stop_motors()
            if current_infrared_right_state == 0 and current_infrared_left_state == 0:
                pwm_valueR = map_user_input(17)
                pwm_valueG = map_user_input(236)
                pwm_valueB = map_user_input(229)
                set_rgb_led(pwm_red_right, pwm_green_right, pwm_blue_right, 0, 0,
                            0)  # Green color
                set_rgb_led(pwm_red_left, pwm_green_left, pwm_blue_left, 0, 0, 0)  # Green color
                stop_motors()
            if current_infrared_left_state == 1 and current_infrared_right_state == 1:
                pwm_valueR = map_user_input(17)
                pwm_valueG = map_user_input(236)
                pwm_valueB = map_user_input(229)
                set_rgb_led(pwm_red_right, pwm_green_right, pwm_blue_right, 0, 0, 0
                            )  # Green color
                set_rgb_led(pwm_red_left, pwm_green_left, pwm_blue_left, 0, 0, 0)  # Green color
                stop_motors()
        if distance_cm > 5 and distance_cm < 20:
            # Forward
            pwm_value = map_user_input(255)
            set_rgb_led(pwm_red_right, pwm_green_right, pwm_blue_right, 0, pwm_value, 0)  # Green color
            set_rgb_led(pwm_red_left, pwm_green_left, pwm_blue_left, 0, pwm_value, 0)  # Green color
            forward()

        elif distance_cm > 20 and distance_cm < 40:
            # Backward
            pwm_value = map_user_input(255)
            set_rgb_led(pwm_red_right, pwm_green_right, pwm_blue_right, pwm_value, 0, 0)  # Red color
            set_rgb_led(pwm_red_left, pwm_green_left, pwm_blue_left, pwm_value, 0, 0)  # Red color
            backward()

    except ValueError:
        print("Invalid input. Please enter a valid number.")
