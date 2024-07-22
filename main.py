import machine
import utime

# Pin configuration
ultrasonic_trigger = machine.Pin(14, machine.Pin.OUT)
ultrasonic_echo = machine.Pin(15, machine.Pin.IN)

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

# Set PWM frequency
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
    ultrasonic_trigger.low()
    utime.sleep_us(2)
    ultrasonic_trigger.high()
    utime.sleep_us(10)
    ultrasonic_trigger.low()

    while ultrasonic_echo.value() == 0:
        signaloff = utime.ticks_us()
    while ultrasonic_echo.value() == 1:
        signalon = utime.ticks_us()

    time_passed = signalon - signaloff
    distance = (time_passed * 0.0343) / 2
    return distance


# Function to control LED brightness based on distance
def control_red_leds_by_distance():
    print("Controlling Red LEDs by Distance")
    for _ in range(500):
        distance = measure_distance()
        print("Distance:", distance)
        if distance <= 2:
            pwm_value = 0
        elif distance >= 20:
            pwm_value = 65535
        else:
            pwm_value = int((distance / 20) * 65535)

        led_left_red.duty_u16(pwm_value)
        led_right_red.duty_u16(pwm_value)
        utime.sleep(0.01)
    utime.sleep(5)
    led_left_red.duty_u16(0)
    led_right_red.duty_u16(0)


# Function to control blue LEDs based on infrared sensors
def control_blue_leds_by_infrared():
    print("Controlling Blue LEDs by Infrared Sensors")
    for _ in range(500):
        left_value = infrared_left.value()
        right_value = infrared_right.value()
        print("Infrared Left:", left_value, "Infrared Right:", right_value)

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
    print("Controlling Motors and Green LEDs")

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
        print("Distance (Left Motor):", distance)
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
        print("Distance (Right Motor):", distance)
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
