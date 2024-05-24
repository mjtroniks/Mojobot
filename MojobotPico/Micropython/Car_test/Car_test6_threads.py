from machine import Pin, PWM, time_pulse_us
import machine
import utime
import _thread  # Import the threading module

# Ultrasonic sensor pins
trigger_pin = Pin(14, Pin.OUT)
echo_pin = Pin(15, Pin.IN)

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

# Shared variable to store distance
distance_cm = 0

# Lock to prevent race conditions
distance_lock = _thread.allocate_lock()


def measure_distance():
    global distance_cm
    while True:
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

        with distance_lock:
            distance_cm = round(distance)
        utime.sleep(0.1)  # Adjust sleep duration as needed


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


def main_control():
    global distance_cm
    while True:
        with distance_lock:
            current_distance = distance_cm

        tracking_state = get_tracking()

        if current_distance > 3:
            if tracking_state == 0:
                timer = utime.ticks_ms()  # Start timer when both sensors detect white
                while utime.ticks_diff(utime.ticks_ms(), timer) < 500 and tracking_state == 0:
                    tracking_state = get_tracking()
                    motors_speed(30, -30)  # Rotate in one direction
                    left_led_pin.off()
                    right_led_pin.off()
                    left_blue_led_pin.on()
                    right_blue_led_pin.on()
                timer = utime.ticks_ms()
                while utime.ticks_diff(utime.ticks_ms(), timer) < 1000 and tracking_state == 0:
                    tracking_state = get_tracking()
                    motors_speed(-30, 30)  # Switch direction
                    left_led_pin.off()
                    right_led_pin.off()
                    left_blue_led_pin.on()
                    right_blue_led_pin.on()

            elif tracking_state == 10:
                tracking_state = get_tracking()
                motors_speed(-30, 30)  # Turn right
                left_led_pin.off()
                right_led_pin.on()

            elif tracking_state == 1:
                tracking_state = get_tracking()
                motors_speed(30, -30)  # Turn left
                left_led_pin.on()
                right_led_pin.off()

            elif tracking_state == 11:
                tracking_state = get_tracking()
                motors_speed(50, 50)  # Move forward
                left_led_pin.on()
                right_led_pin.on()
        else:
            tracking_state = get_tracking()
            motors_speed(0, 0)  # Stop motors


# Start the ultrasonic sensor measurement on the second core
_thread.start_new_thread(measure_distance, ())

# Run the main control loop on the first core
main_control()
