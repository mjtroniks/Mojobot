import machine
from machine import Pin, PWM, time_pulse_us
import utime
##################Ultrasonic##############################
# Ultrasonic sensor pins
trigger_pin = Pin(14, Pin.OUT)
echo_pin = Pin(15, Pin.IN)
#######################Leds###############################
led_red_right = Pin(22)
led_green_right = Pin(20)
led_blue_right = Pin(21)

# Set up PWM for the right RGB LED
pwm_red_right = PWM(led_red_right)
pwm_green_right = PWM(led_green_right)
pwm_blue_right = PWM(led_blue_right)

# Define the LED pins for the left RGB LED
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
###################Motors#######################################
# Motor 1
motor1_pwm_pin = Pin(10)
motor1_dir_pin = Pin(12, machine.Pin.OUT)
motor1_pwm = PWM(motor1_pwm_pin, freq=1000)  # Explicitly set frequency for isolation

# Motor 2
motor2_pwm_pin = Pin(11)
motor2_dir_pin = Pin(13, machine.Pin.OUT)
motor2_pwm = PWM(motor2_pwm_pin, freq=1000)  # Explicitly set frequency for isolation
##################Infrared#########################
# Line following sensors
sensor1_pin = Pin(2, Pin.IN)#left IR
sensor2_pin = Pin(3, Pin.IN)#right IR

# Previous sensor states
prev_sensor1_state = sensor1_pin.value()
prev_sensor2_state = sensor2_pin.value()

#################Functions#############################
def map_user_input(user_input):
    # Ensure user_input is within the valid range
    user_input = max(0, min(255, user_input))
    # Map the value to the PWM range
    return int((user_input / 255) * 65535)

def set_rgb_led(pwm_red, pwm_green, pwm_blue, r_value, g_value, b_value):
    pwm_red.duty_u16(r_value)
    pwm_green.duty_u16(g_value)
    pwm_blue.duty_u16(b_value)

def turn_off_leds(pwm_red, pwm_green, pwm_blue):
    pwm_red.duty_u16(0)
    pwm_green.duty_u16(0)
    pwm_blue.duty_u16(0)

def map_speed_to_pwm(speed):
    # Ensure speed is within the valid range
    speed = max(0, min(100, speed))
    # Map the speed to the PWM range
    return int((speed / 100) * 65535)

def forward():
    motor1_dir_pin.on()
    motor2_dir_pin.on()
    motor1_pwm.duty_u16(speed_pwm)
    motor2_pwm.duty_u16(speed_pwm)

def backward():
    motor1_dir_pin.off()
    motor2_dir_pin.off()
    motor1_pwm.duty_u16(speed_pwm)
    motor2_pwm.duty_u16(speed_pwm)

def stop_motors():
    motor1_pwm.duty_u16(0)
    motor2_pwm.duty_u16(0)



def get_distance():
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
#####################Main Program######################
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
        current_sensor1_state = sensor1_pin.value()#left infrared sensor
        current_sensor2_state = sensor2_pin.value()#right infrared sensor
        print("Sensor left "+str(current_sensor1_state)+"  Sensor right "+str(current_sensor2_state))
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

        else:
            # Stop
            turn_off_leds(pwm_red_right, pwm_green_right, pwm_blue_right)
            turn_off_leds(pwm_red_left, pwm_green_left, pwm_blue_left)
            stop_motors()

    except ValueError:
        print("Invalid input. Please enter a valid number.")
