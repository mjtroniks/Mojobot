from machine import Pin, PWM
from time import sleep
import machine

# Motor 1
motor1_pwm_pin = Pin(10)
motor1_dir_pin = Pin(12, machine.Pin.OUT)
motor1_pwm = PWM(motor1_pwm_pin)

# Motor 2
motor2_pwm_pin = Pin(11)
motor2_dir_pin = Pin(13, machine.Pin.OUT)
motor2_pwm = PWM(motor2_pwm_pin)

# Set PWM frequency for motors
pwm_frequency = 1000
motor1_pwm.freq(pwm_frequency)
motor2_pwm.freq(pwm_frequency)

def motors_speed(left_wheel_speed,right_wheel_speed):


    if left_wheel_speed > 0:
        motor1_dir_pin.on()
    else:
        motor1_dir_pin.off()

    if right_wheel_speed > 0:
        motor2_dir_pin.on()
    else:
        motor2_dir_pin.off()
    left_wheel_speed = left_wheel_speed if left_wheel_speed > 0 else left_wheel_speed * -1
    left_wheel_speed = max(0, min(100, left_wheel_speed))
    left_wheel_speed = int((left_wheel_speed / 100) * 65535)
    motor1_pwm.duty_u16(left_wheel_speed)

    right_wheel_speed = right_wheel_speed if right_wheel_speed > 0 else right_wheel_speed * -1
    right_wheel_speed = max(0, min(100, right_wheel_speed))
    right_wheel_speed = int((right_wheel_speed / 100) * 65535)
    motor2_pwm.duty_u16(right_wheel_speed)

motors_speed(30,30)
