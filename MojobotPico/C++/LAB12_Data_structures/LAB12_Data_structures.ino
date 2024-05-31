#include <Arduino.h>

// Define functions
int get_tracking();
long measure_distance();
void motors_speed(int left_wheel_speed, int right_wheel_speed);

// Ultrasonic sensor pins
const int trigger_pin = 14;
const int echo_pin = 15;
const int left_sensor_pin = 3;
const int right_sensor_pin = 2;

// Motor pins and configuration
struct MotorPins {
    int motor1_pwm;
    int motor1_dir;
    int motor2_pwm;
    int motor2_dir;
};

MotorPins motor_pins = {10, 12, 11, 13};

// LED pins
int led_pins[] = {22, 7, 20, 9};  // {left_led, right_led, left_blue_led, right_blue_led}

// Set up PWM for motors
const int pwm_frequency = 1000;

void setup() {
    // Initialize serial communication
    Serial.begin(115200);

    // Initialize ultrasonic sensor pins
    pinMode(trigger_pin, OUTPUT);
    pinMode(echo_pin, INPUT);

    // Initialize line follower sensor pins
    pinMode(left_sensor_pin, INPUT);
    pinMode(right_sensor_pin, INPUT);

    // Initialize motor pins
    pinMode(motor_pins.motor1_pwm, OUTPUT);
    pinMode(motor_pins.motor1_dir, OUTPUT);
    pinMode(motor_pins.motor2_pwm, OUTPUT);
    pinMode(motor_pins.motor2_dir, OUTPUT);

    // Initialize LED pins
    for (int i = 0; i < 4; i++) {
        pinMode(led_pins[i], OUTPUT);
    }

    // Set PWM frequency for motors
    analogWriteFreq(pwm_frequency);
}

void loop() {
    int tracking_state = get_tracking();
    long distance_cm = measure_distance();
    if (distance_cm > 3) {
        if (tracking_state == 0 || tracking_state == 1 || tracking_state == 2 || tracking_state == 3) {
            int motor_speeds[4][2] = {{-20, 20}, {30, -30}, {-30, 30}, {50, 50}};
            int tracking_states[4] = {0, 1, 2, 3};
            for (int i = 0; i < 4; i++) {
                if (tracking_state == tracking_states[i]) {
                    motors_speed(motor_speeds[i][0], motor_speeds[i][1]);
                    if (tracking_state == 2) {
                        digitalWrite(led_pins[0], LOW);  // left_led_pin
                        digitalWrite(led_pins[1], HIGH);  // right_led_pin
                    } else if (tracking_state == 1) {
                        digitalWrite(led_pins[0], HIGH);  // left_led_pin
                        digitalWrite(led_pins[1], LOW);  // right_led_pin
                    } else if (tracking_state == 3) {
                        digitalWrite(led_pins[0], HIGH);  // left_led_pin
                        digitalWrite(led_pins[1], HIGH);  // right_led_pin
                    }
                    delay(200);
                    break;
                }
            }
        }
    } else {
        motors_speed(0, 0);  // Stop
    }
}

// Define function implementations

int get_tracking() {
    // Implement the function to get tracking information
    // Example implementation:
    int left = digitalRead(left_sensor_pin);
    int right = digitalRead(right_sensor_pin);
    return (left << 1) | right;  // Combine left and right sensor values
}

long measure_distance() {
    // Implement the function to measure distance
    // Example implementation:
    digitalWrite(trigger_pin, LOW);
    delayMicroseconds(2);
    digitalWrite(trigger_pin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigger_pin, LOW);

    long duration = pulseIn(echo_pin, HIGH);
    long distance_cm = duration * 0.034 / 2;  // Speed of sound = 0.034 cm/us
    return distance_cm;
}

void motors_speed(int left_wheel_speed, int right_wheel_speed) {
    // Implement the function to control motor speed
    // Example implementation:
    analogWrite(motor_pins.motor1_pwm, abs(left_wheel_speed));
    digitalWrite(motor_pins.motor1_dir, left_wheel_speed > 0 ? HIGH : LOW);

    analogWrite(motor_pins.motor2_pwm, abs(right_wheel_speed));
    digitalWrite(motor_pins.motor2_dir, right_wheel_speed > 0 ? HIGH : LOW);
}
