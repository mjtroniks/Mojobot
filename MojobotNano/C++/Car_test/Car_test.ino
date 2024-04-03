#include <ArduinoBLE.h>

// Define pins for sensors
const int left_sensor_pin = 5;   // Infrared sensor left connected to D5
const int right_sensor_pin = 4;  // Infrared sensor right connected to D4

// Define pins for motors
const int motor_left_pwm_pin = 7;    // PWM motor left connected to D7
const int motor_right_pwm_pin = 6;   // PWM motor right connected to D6
const int motor_left_dir_pin = 8;     // Direction motor left connected to D8
const int motor_right_dir_pin = 9;    // Direction motor right connected to D9

// Define pins for LEDs
const int left_led_red_pin = A2;
const int left_led_blue_pin = A3;
const int left_led_green_pin = 10;   // Green LED left connected to D10

const int right_led_red_pin = 11;    // Red LED right connected to D11
const int right_led_blue_pin = A6;
const int right_led_green_pin = A7;  // Green LED right connected to A7

void setup() {
    // Initialize pins for sensors
    pinMode(left_sensor_pin, INPUT);
    pinMode(right_sensor_pin, INPUT);

    // Initialize pins for motors
    pinMode(motor_left_pwm_pin, OUTPUT);
    pinMode(motor_right_pwm_pin, OUTPUT);
    pinMode(motor_left_dir_pin, OUTPUT);
    pinMode(motor_right_dir_pin, OUTPUT);

    // Initialize pins for LEDs
    pinMode(left_led_red_pin, OUTPUT);
    pinMode(left_led_blue_pin, OUTPUT);
    pinMode(left_led_green_pin, OUTPUT);
    pinMode(right_led_red_pin, OUTPUT);
    pinMode(right_led_blue_pin, OUTPUT);
    pinMode(right_led_green_pin, OUTPUT);
}

void motors_speed(int left_wheel_speed, int right_wheel_speed) {
    // Control direction
    digitalWrite(motor_left_dir_pin, left_wheel_speed > 0 ? HIGH : LOW);
    digitalWrite(motor_right_dir_pin, right_wheel_speed > 0 ? HIGH : LOW);

    // Set PWM duty cycle
    int left_pwm_value = map(constrain(abs(left_wheel_speed), 0, 100), 0, 100, 0, 255);
    int right_pwm_value = map(constrain(abs(right_wheel_speed), 0, 100), 0, 100, 0, 255);
    analogWrite(motor_left_pwm_pin, left_pwm_value);
    analogWrite(motor_right_pwm_pin, right_pwm_value);
}

int get_tracking() {
    int left = digitalRead(left_sensor_pin);
    int right = digitalRead(right_sensor_pin);

    if (left == 1 && right == 1)
        return 0;
    else if (left == 0 && right == 1)
        return 10;
    else if (left == 1 && right == 0)
        return 1;
    else if (left == 0 && right == 0)
        return 11;
    else {
        Serial.println("Unknown ERROR");
        return -1;
    }
}

void loop() {
    int tracking_state = get_tracking();

    switch (tracking_state) {
        case 10:
            Serial.println("Left triggered");
            motors_speed(30, 5);
            digitalWrite(left_led_red_pin, HIGH);
            digitalWrite(left_led_blue_pin, LOW);
            digitalWrite(left_led_green_pin, LOW);
            digitalWrite(right_led_red_pin, LOW);
            digitalWrite(right_led_blue_pin, LOW);
            digitalWrite(right_led_green_pin, LOW);
            break;
        case 1:
            Serial.println("Right triggered");
            motors_speed(5, 30);
            digitalWrite(left_led_red_pin, LOW);
            digitalWrite(left_led_blue_pin, LOW);
            digitalWrite(left_led_green_pin, LOW);
            digitalWrite(right_led_red_pin, HIGH);
            digitalWrite(right_led_blue_pin, LOW);
            digitalWrite(right_led_green_pin, LOW);
            break;
        case 0:
            Serial.println("Both triggered");
            motors_speed(30, 30);
            digitalWrite(left_led_red_pin, HIGH);
            digitalWrite(left_led_blue_pin, LOW);
            digitalWrite(left_led_green_pin, LOW);
            digitalWrite(right_led_red_pin, HIGH);
            digitalWrite(right_led_blue_pin, LOW);
            digitalWrite(right_led_green_pin, LOW);
            break;
        default:
            break;
    }
    //delay(100); // Adjust delay as needed
}
