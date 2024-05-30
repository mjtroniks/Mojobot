from machine import Pin, PWM, time_pulse_us
import utime
import random


class Motors:
    def __init__(self, pwm_pin1, dir_pin1, pwm_pin2, dir_pin2, pwm_frequency):
        self.motor1_pwm_pin = pwm_pin1
        self.motor1_dir_pin = dir_pin1
        self.motor2_pwm_pin = pwm_pin2
        self.motor2_dir_pin = dir_pin2
        self.motor1_pwm = PWM(Pin(self.motor1_pwm_pin))
        self.motor1_dir = Pin(self.motor1_dir_pin, Pin.OUT)
        self.motor2_pwm = PWM(Pin(self.motor2_pwm_pin))
        self.motor2_dir = Pin(self.motor2_dir_pin, Pin.OUT)
        self.motor1_pwm.freq(pwm_frequency)
        self.motor2_pwm.freq(pwm_frequency)

    def motors_speed(self, left_speed, right_speed):
        self.motor1_dir.value(1 if left_speed > 0 else 0)
        self.motor2_dir.value(1 if right_speed > 0 else 0)
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
        pulse_width = time_pulse_us(self.echo_pin, 1, 30000)
        distance = pulse_width * 0.034 / 2
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


class Robot:
    def __init__(self, pwm_frequency):
        # Initialize LED pins
        self.left_led_pin = Pin(22, Pin.OUT)
        self.right_led_pin = Pin(7, Pin.OUT)

        # Initialize sensor pins
        self.trigger_pin = 14
        self.echo_pin = 15
        self.left_sensor_pin = 3
        self.right_sensor_pin = 2

        # Initialize motor pins
        self.motor1_pwm_pin = 10
        self.motor1_dir_pin = 12
        self.motor2_pwm_pin = 11
        self.motor2_dir_pin = 13

        # Set PWM frequency for motors
        self.pwm_frequency = pwm_frequency

        # Initialize motors and sensors
        self.motors = Motors(pwm_pin1=self.motor1_pwm_pin, dir_pin1=self.motor1_dir_pin, pwm_pin2=self.motor2_pwm_pin,
                             dir_pin2=self.motor2_dir_pin, pwm_frequency=self.pwm_frequency)
        self.sensors = Sensors(self.trigger_pin, self.echo_pin, self.left_sensor_pin, self.right_sensor_pin)

    def generate_random_20(self):
        return random.choice([-20, 20])

    def run(self):
        while True:
            tracking_state = self.sensors.get_tracking()
            distance_cm = self.sensors.measure_distance()
            utime.sleep_ms(10)
            print(distance_cm)
            if distance_cm > 3:
                if tracking_state == 0:
                    tracking_state = self.sensors.get_tracking()
                    speed = self.generate_random_20()
                    self.motors.motors_speed(speed, -speed)
                    utime.sleep_ms(200)
                elif tracking_state == 10:
                    tracking_state = self.sensors.get_tracking()
                    self.motors.motors_speed(-30, 30)
                    self.left_led_pin.off()
                    self.right_led_pin.on()
                elif tracking_state == 1:
                    tracking_state = self.sensors.get_tracking()
                    self.motors.motors_speed(30, -30)
                    self.left_led_pin.on()
                    self.right_led_pin.off()
                elif tracking_state == 11:
                    tracking_state = self.sensors.get_tracking()
                    self.motors.motors_speed(50, 50)
                    self.left_led_pin.on()
                    self.right_led_pin.on()
            else:
                tracking_state = self.sensors.get_tracking()
                self.motors.motors_speed(0, 0)
class CarRobot(Robot):
    def __init__(self, pwm_frequency):
        super().__init__(pwm_frequency)

    # Any additional methods or overrides for CarRobot can go here
# Instantiate the CarRobot and run it
car_robot = CarRobot(pwm_frequency=1000)
car_robot.run()
