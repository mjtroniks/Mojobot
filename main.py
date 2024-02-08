from machine import Pin, PWM
from time import sleep
import machine

# Sensor pins
left_sensor_pin = Pin(2, Pin.IN)
right_sensor_pin = Pin(3, Pin.IN)

# Motor 1 pins
motor1_pwm_pin = Pin(10)
motor1_dir_pin = Pin(12, machine.Pin.OUT)
motor1_pwm = PWM(motor1_pwm_pin)

# Motor 2 pins
motor2_pwm_pin = Pin(11)
motor2_dir_pin = Pin(13, machine.Pin.OUT)
motor2_pwm = PWM(motor2_pwm_pin)

# LED pins
left_led_pin = Pin(7, Pin.OUT)
right_led_pin = Pin(22, Pin.OUT)

blueR = Pin(21, Pin.OUT)
blueL = Pin(9, Pin.OUT)

# Set PWM frequency for motors
pwm_frequency = 1000
motor1_pwm.freq(pwm_frequency)
motor2_pwm.freq(pwm_frequency)

def motors_speed(left_wheel_speed, right_wheel_speed):
    # Control direction
    motor1_dir_pin.value(1 if left_wheel_speed > 0 else 0)
    motor2_dir_pin.value(1 if right_wheel_speed > 0 else 0)

    # Set PWM duty cycle
    left_wheel_speed = max(0, min(100, abs(left_wheel_speed)))
    left_wheel_speed = int((left_wheel_speed / 100) * 65535)
    motor1_pwm.duty_u16(left_wheel_speed)

    right_wheel_speed = max(0, min(100, abs(right_wheel_speed)))
    right_wheel_speed = int((right_wheel_speed / 100) * 65535)
    motor2_pwm.duty_u16(right_wheel_speed)

def get_tracking():
    left = left_sensor_pin.value()
    right = right_sensor_pin.value()

    if left == 1 and right == 1:
        return 0
    elif left == 0 and right == 1:
        return 10
    elif left == 1 and right == 0:
        return 1
    elif left == 0 and right == 0:
        return 11
    else:
        print("Unknown ERROR")

while True:
    tracking_state = get_tracking()
    print("State",tracking_state)
    lastState = 0
    if tracking_state == 10:
        print("Left triggered")
        motors_speed(5, 30)
        left_led_pin.on()
        right_led_pin.off()  # Turn on right LED
        lastState = tracking_state
    elif tracking_state == 1:
        print("Right triggered")
        motors_speed(30, 5)
        left_led_pin.off()  # Turn on left LED
        right_led_pin.on()
        lastState = tracking_state
    elif tracking_state == 11:
        print("Both triggered")

        if lastState == 1:
            print("Off track")
            motors_speed(30, 5)
            left_led_pin.off()
            right_led_pin.off()  # Turn off both LEDs
        elif lastState == 10:
            print("Off track")
            motors_speed(5, 30)
            left_led_pin.off()
            right_led_pin.off()  # Turn off both LEDs
        elif lastState == 11:
            print("Off track")
            motors_speed(5, 30)
            left_led_pin.off()
            right_led_pin.off()  # Turn off both LEDs
        lastState = tracking_state
    elif tracking_state == 00:
        if lastState == 1:
            print("Off track")
            motors_speed(30, 5)
            left_led_pin.off()
            right_led_pin.off()  # Turn off both LEDs
        elif lastState == 10:
            print("Off track")
            motors_speed(5, 30)
            left_led_pin.off()
            right_led_pin.off()  # Turn off both LEDs
        elif lastState == 11:
            print("Off track")
            motors_speed(5, 30)
            left_led_pin.off()
            right_led_pin.off()  # Turn off both LEDs



    #sleep(0.1)  # Adjust the delay as needed for your application
