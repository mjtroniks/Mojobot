#include <Arduino.h>

// Ultrasonic sensor pins
const int TRIGGER_PIN = 14;
const int ECHO_PIN = 15;

// Line follower sensor pins
const int LEFT_SENSOR_PIN = 3;
const int RIGHT_SENSOR_PIN = 2;

// Motor 1 pins
const int MOTOR1_PWM_PIN = 10;
const int MOTOR1_DIR_PIN = 12;

// Motor 2 pins
const int MOTOR2_PWM_PIN = 11;
const int MOTOR2_DIR_PIN = 13;

// LEDs pins
const int LED_PIN_LEFT = 22;
const int LED_PIN_RIGHT = 7;
const int LED_PIN_LEFT_BLUE = 20;
const int LED_PIN_RIGHT_BLUE = 9;

// Set PWM frequency for motors
const int PWM_FREQUENCY = 1000;

// Function to measure distance using ultrasonic sensor
long measure_distance() {
    digitalWrite(TRIGGER_PIN, LOW);
    delayMicroseconds(2);
    digitalWrite(TRIGGER_PIN, HIGH);
    delayMicroseconds(10);
    digitalWrite(TRIGGER_PIN, LOW);
    long duration = pulseIn(ECHO_PIN, HIGH);
    long distance_cm = duration * 0.034 / 2;
    return distance_cm;
}

// Function to set motor speeds
void motors_speed(int left_wheel_speed, int right_wheel_speed) {
    if (left_wheel_speed > 0) {
    digitalWrite(MOTOR1_DIR_PIN, HIGH);
  } else {
    digitalWrite(MOTOR1_DIR_PIN, LOW);
  }

  if (right_wheel_speed > 0) {
    digitalWrite(MOTOR2_DIR_PIN, HIGH);
  } else {
    digitalWrite(MOTOR2_DIR_PIN, LOW);
  }

  left_wheel_speed = abs(left_wheel_speed);
  left_wheel_speed = constrain(left_wheel_speed, 0, 100);
  int left_pwm_value = map(left_wheel_speed, 0, 100, 0, 255);
  analogWrite(MOTOR1_PWM_PIN, left_pwm_value);

  right_wheel_speed = abs(right_wheel_speed);
  right_wheel_speed = constrain(right_wheel_speed, 0, 100);
  int right_pwm_value = map(right_wheel_speed, 0, 100, 0, 255);
  analogWrite(MOTOR2_PWM_PIN, right_pwm_value);
}

// Function to get tracking sensor state
int get_tracking() {
    int leftSensor = digitalRead(LEFT_SENSOR_PIN);
    int rightSensor = digitalRead(RIGHT_SENSOR_PIN);

    if (leftSensor == LOW && rightSensor == LOW) {
        return 0;
    } else if (leftSensor == LOW && rightSensor == HIGH) {
        return 1;
    } else if (leftSensor == HIGH && rightSensor == LOW) {
        return 10;
    } else if (leftSensor == HIGH && rightSensor == HIGH) {
        return 11;
    }
    // Default return statement if none of the conditions are met
    return -1; // or any other appropriate value
}
// Function to generate random value of -20 or 20
int generate_random_20() {
    // Seed the random number generator
    randomSeed(analogRead(0)); // You can use any analog pin for seeding

    // Generate a random value of -20 or 20
    return random(2) ? -20 : 20;
}

void setup() {
    // Initialize serial communication
    Serial.begin(115200);

    // Initialize ultrasonic sensor pins
    pinMode(TRIGGER_PIN, OUTPUT);
    pinMode(ECHO_PIN, INPUT);

    // Initialize line follower sensor pins
    pinMode(LEFT_SENSOR_PIN, INPUT);
    pinMode(RIGHT_SENSOR_PIN, INPUT);

    // Initialize motor pins
    pinMode(MOTOR1_PWM_PIN, OUTPUT);
    pinMode(MOTOR1_DIR_PIN, OUTPUT);
    pinMode(MOTOR2_PWM_PIN, OUTPUT);
    pinMode(MOTOR2_DIR_PIN, OUTPUT);

    // Initialize LED pins
    pinMode(LED_PIN_LEFT, OUTPUT);
    pinMode(LED_PIN_RIGHT, OUTPUT);
    pinMode(LED_PIN_LEFT_BLUE, OUTPUT);
    pinMode(LED_PIN_RIGHT_BLUE, OUTPUT);
}

void loop() {
    int tracking_state = get_tracking();
    long distance_cm = measure_distance();

    if (distance_cm > 3) {
        if (tracking_state == 0) {
            // No line detected
            // No line detected
            digitalWrite(LED_PIN_LEFT, LOW);
            digitalWrite(LED_PIN_RIGHT, LOW);
            int speed = generate_random_20();
            motors_speed(speed, -speed);  // Turn right
            delay(200);
        }
        else if (tracking_state == 1) {
            // Left sensor on line
            digitalWrite(LED_PIN_LEFT, HIGH);
            digitalWrite(LED_PIN_RIGHT, LOW);
            motors_speed(30, -30);  // Turn right
        }
        else if (tracking_state == 10) {
            // Right sensor on line
            digitalWrite(LED_PIN_LEFT, LOW);
            digitalWrite(LED_PIN_RIGHT, HIGH);
            motors_speed(-30, 30);  // Turn left
        }
        else if (tracking_state == 11) {
            // Both sensors on line
            digitalWrite(LED_PIN_LEFT, HIGH);
            digitalWrite(LED_PIN_RIGHT, HIGH);
            motors_speed(30, 30);  // Move forward
        }
    } else {
        // Obstacle detected
        digitalWrite(LED_PIN_LEFT, HIGH);
        digitalWrite(LED_PIN_RIGHT, HIGH);
        motors_speed(0, 0);  // Stop motors
    }

    delay(100);  // Adjust delay as needed
}
