from machine import Pin, PWM, time_pulse_us
import utime
import random


class Motors:
    def __init__(self, pwm_pin1, dir_pin1, pwm_pin2, dir_pin2, pwm_frequency):
        self.motor1_pwm_pin = pwm_pin1
        self.motor1_dir_pin = dir_pin1
        self.motor2_pwm_pin = pwm_pin2
        self.motor2_dir_pin = dir_pin2
        self.pwm_frequency = pwm_frequency

        # Initialize PWM objects for motors
        self.motor1_pwm = PWM(Pin(self.motor1_pwm_pin))
        self.motor2_pwm = PWM(Pin(self.motor2_pwm_pin))

        # Set PWM frequency for motors
        self.motor1_pwm.freq(self.pwm_frequency)
        self.motor2_pwm.freq(self.pwm_frequency)

        # Initialize direction pins
        self.motor1_dir = Pin(self.motor1_dir_pin, Pin.OUT)
        self.motor2_dir = Pin(self.motor2_dir_pin, Pin.OUT)

    def motors_speed(self, left_speed, right_speed):
        # Control direction
        self.motor1_dir.value(1 if left_speed > 0 else 0)
        self.motor2_dir.value(1 if right_speed > 0 else 0)

        # Set PWM duty cycle
        left_speed = max(0, min(100, abs(left_speed)))
        left_duty_cycle = int((left_speed / 100) * 65535)
        self.motor1_pwm.duty_u16(left_duty_cycle)

        right_speed = max(0, min(100, abs(right_speed)))
        right_duty_cycle = int((right_speed / 100) * 65535)
        self.motor2_pwm.duty_u16(right_duty_cycle)


class Sensors:
    def __init__(self, trigger_pin, echo_pin, left_sensor_pin, right_sensor_pin):
        self.trigger_pin = Pin(trigger_pin, Pin.OUT)
        self.echo_pin = Pin(echo_pin, Pin.IN)
        self.left_sensor_pin = Pin(left_sensor_pin, Pin.IN)
        self.right_sensor_pin = Pin(right_sensor_pin, Pin.IN)

    def measure_distance(self):
        self.trigger_pin.off()
        utime.sleep_us(2)
        self.trigger_pin.on()
        utime.sleep_us(10)
        self.trigger_pin.off()

        pulse_width = time_pulse_us(self.echo_pin, 1, 30000)  # 30ms timeout (max range)
        distance = pulse_width * 0.034 / 2  # Speed of sound = 0.034 cm/us
        return round(distance)

    def get_tracking(self):
        left = self.left_sensor_pin.value()
        right = self.right_sensor_pin.value()

        if left == 0 and right == 0:
            return 0
        elif left == 0 and right == 1:
            return 1
        elif left == 1 and right == 0:
            return 10
        elif left == 1 and right == 1:
            return 11


# LED pins
left_led_pin = Pin(22, Pin.OUT)
right_led_pin = Pin(7, Pin.OUT)

# Ultrasonic sensor pins
trigger_pin = 14
echo_pin = 15

# Sensor pins
left_sensor_pin = 3
right_sensor_pin = 2

# Motor 1 pins
motor1_pwm_pin = 10
motor1_dir_pin = 12

# Motor 2 pins
motor2_pwm_pin = 11
motor2_dir_pin = 13

# Set PWM frequency for motors
pwm_frequency = 1000

# Initialize motors
motors = Motors(pwm_pin1=motor1_pwm_pin, dir_pin1=motor1_dir_pin, pwm_pin2=motor2_pwm_pin, dir_pin2=motor2_dir_pin,
                pwm_frequency=pwm_frequency)

# Initialize ultrasonic sensor
sensors = Sensors(trigger_pin, echo_pin, left_sensor_pin, right_sensor_pin)


def generate_random_20():
    return random.choice([-15, 15])


while True:
    tracking_state = sensors.get_tracking()
    distance_cm = sensors.measure_distance()
    utime.sleep_ms(100)  # Adjust sleep duration as needed
    #print(distance_cm)
    if distance_cm > 3:
        if tracking_state == 0:
            #tracking_state = sensors.get_tracking()
            speed = generate_random_20()
            motors.motors_speed(speed, -speed)  # Turn right
            utime.sleep_ms(200)
            tracking_state = sensors.get_tracking()
            left_led_pin.off()  # Turn on left LED
            right_led_pin.off()  # Turn on right LED

        elif tracking_state == 10:

            motors.motors_speed(-15, 15)  # Turn right
            left_led_pin.off()
            right_led_pin.on()  # Turn on right LED
            tracking_state = sensors.get_tracking()
        elif tracking_state == 1:

            motors.motors_speed(15, -15)  # Turn left
            left_led_pin.on()  # Turn on left LED
            right_led_pin.off()
            tracking_state = sensors.get_tracking()
        elif tracking_state == 11:

            motors.motors_speed(20, 20)  # Move forward
            left_led_pin.on()  # Turn on left LED
            right_led_pin.on()  # Turn on right LED
            tracking_state = sensors.get_tracking()
    else:
        tracking_state = sensors.get_tracking()
        motors.motors_speed(0, 0)  # Turn left
