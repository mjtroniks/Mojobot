from machine import Pin, PWM
import machine
import utime

# Sensor pins
left_sensor_pin = Pin(3, Pin.IN)
right_sensor_pin = Pin(2, Pin.IN)

# Motor 1 pins
motor1_pwm_pin = Pin(10)
motor1_dir_pin = Pin(12, machine.Pin.OUT)
motor1_pwm = PWM(motor1_pwm_pin)

# Motor 2 pins
motor2_pwm_pin = Pin(11)
motor2_dir_pin = Pin(13, machine.Pin.OUT)
motor2_pwm = PWM(motor2_pwm_pin)

# LED pins
left_led_pin = Pin(22, Pin.OUT)
right_led_pin = Pin(7, Pin.OUT)
left_blue_led_pin = Pin(20, Pin.OUT)
right_blue_led_pin = Pin(9, Pin.OUT)
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

    if left == 0 and right == 0:
        return 0
    elif left == 0 and right == 1:
        return 1
    elif left == 1 and right == 0:
        return 10
    elif left == 1 and right == 1:
        return 11

while True:
    tracking_state = get_tracking()

    if tracking_state == 0:
        timer = utime.ticks_ms()  # Start timer when both sensors detect white


        while utime.ticks_diff(utime.ticks_ms(), timer) < 1500 and tracking_state == 0:
             tracking_state = get_tracking()
             motors_speed(30, -30)  # Rotate in one direction
             left_led_pin.off()
             right_led_pin.off()  # Turn on right LED
             left_blue_led_pin.on()#
             right_blue_led_pin.on()
        timer = utime.ticks_ms()  # Start timer when both sensors detect white

        while utime.ticks_diff(utime.ticks_ms(), timer) < 3000 and tracking_state == 0:
             tracking_state = get_tracking()
             motors_speed(-30, 30)  # Switch direction
             left_led_pin.off()
             right_led_pin.off()  # Turn on right LED
             left_blue_led_pin.on()  #
             right_blue_led_pin.on()

    elif tracking_state == 10:
        motors_speed(-30, 30)  # Turn right
        left_led_pin.off()
        right_led_pin.on()  # Turn on right LED

    elif tracking_state == 1:
        motors_speed(30, -30)  # Turn left
        left_led_pin.on()  # Turn on left LED
        right_led_pin.off()

    elif tracking_state == 11:
        motors_speed(50, 50)  # Move forward
        left_led_pin.on()  # Turn on left LED
        right_led_pin.on()  # Turn on right LED
