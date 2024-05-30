#include <Arduino.h>

// Define motor pins
const int motor1_pwm_pin = 10;
const int motor1_dir_pin = 12;
const int motor2_pwm_pin = 11;
const int motor2_dir_pin = 13;

void setup() {
  // Initialize motor pins
  pinMode(motor1_pwm_pin, OUTPUT);
  pinMode(motor1_dir_pin, OUTPUT);
  pinMode(motor2_pwm_pin, OUTPUT);
  pinMode(motor2_dir_pin, OUTPUT);

  // Set PWM frequency for motors
  int pwm_frequency = 1000;
  analogWriteFreq(pwm_frequency);
}

void motors_speed(int left_wheel_speed, int right_wheel_speed) {
  if (left_wheel_speed > 0) {
    digitalWrite(motor1_dir_pin, HIGH);
  } else {
    digitalWrite(motor1_dir_pin, LOW);
  }

  if (right_wheel_speed > 0) {
    digitalWrite(motor2_dir_pin, HIGH);
  } else {
    digitalWrite(motor2_dir_pin, LOW);
  }

  left_wheel_speed = abs(left_wheel_speed);
  left_wheel_speed = constrain(left_wheel_speed, 0, 100);
  int left_pwm_value = map(left_wheel_speed, 0, 100, 0, 255);
  analogWrite(motor1_pwm_pin, left_pwm_value);

  right_wheel_speed = abs(right_wheel_speed);
  right_wheel_speed = constrain(right_wheel_speed, 0, 100);
  int right_pwm_value = map(right_wheel_speed, 0, 100, 0, 255);
  analogWrite(motor2_pwm_pin, right_pwm_value);
}

void loop() {
  // Example usage
  motors_speed(30, 30);
  delay(1000); // Delay for 1 second
}
