// Define RGB LED pins for the right RGB LED
const int led_red_right = 22;
const int led_green_right = 20;
const int led_blue_right = 21;

// Define RGB LED pins for the left RGB LED
const int led_red_left = 7;
const int led_green_left = 9;
const int led_blue_left = 8;

// Set up PWM for both right and left RGB LEDs
const int frequency = 5000;
const int resolution = 8;
const int led_red_right_channel = 0;
const int led_green_right_channel = 1;
const int led_blue_right_channel = 2;
const int led_red_left_channel = 3;
const int led_green_left_channel = 4;
const int led_blue_left_channel = 5;

// Define Motor 1 pins
const int motor1_pwm_pin = 10;
const int motor1_dir_pin = 12;

// Define Motor 2 pins
const int motor2_pwm_pin = 11;
const int motor2_dir_pin = 13;

// Define Infrared sensors
const int infrared_left_pin = 2;
const int infrared_right_pin = 3;

const int trigger_pin = 14;
const int echo_pin = 15;
int pwm_value;  // Define pwm_value for motor control

void setup() {
  // Set up RGB LEDs
  pinMode(led_red_right, OUTPUT);
  pinMode(led_green_right, OUTPUT);
  pinMode(led_blue_right, OUTPUT);
  pinMode(led_red_left, OUTPUT);
  pinMode(led_green_left, OUTPUT);
  pinMode(led_blue_left, OUTPUT);

  // Set up PWM for RGB LEDs
  analogWriteFrequency(led_red_right_channel, frequency);
  analogWriteFrequency(led_green_right_channel, frequency);
  analogWriteFrequency(led_blue_right_channel, frequency);
  analogWriteFrequency(led_red_left_channel, frequency);
  analogWriteFrequency(led_green_left_channel, frequency);
  analogWriteFrequency(led_blue_left_channel, frequency);

  // Set up Motors
  pinMode(motor1_pwm_pin, OUTPUT);
  pinMode(motor1_dir_pin, OUTPUT);
  pinMode(motor2_pwm_pin, OUTPUT);
  pinMode(motor2_dir_pin, OUTPUT);

  // Set up Infrared sensors
  pinMode(infrared_left_pin, INPUT);
  pinMode(infrared_right_pin, INPUT);
}

void loop() {
  // Main Program
  try {
    int distance_cm = get_distance();
    delay(100);  // To avoid measuring too frequently
    int speed_percent = 40;
    int speed_pwm = map_speed_to_pwm(speed_percent);
    Serial.print("Distance: ");
    Serial.println(distance_cm);

    int current_infrared_left_state = digitalRead(infrared_left_pin);
    int current_infrared_right_state = digitalRead(infrared_right_pin);
    Serial.print("Infrared left: ");
    Serial.print(current_infrared_left_state);
    Serial.print("  Infrared right: ");
    Serial.println(current_infrared_right_state);

    if (distance_cm > 40) {
      if (current_infrared_right_state == 1 && current_infrared_left_state == 0) {
        set_rgb_led(led_red_right, led_green_right, led_blue_right, 17, 236, 229);
        set_rgb_led(led_red_left, led_green_left, led_blue_left, 0, 0, 0);
        stop_motors();
      }
      if (current_infrared_left_state == 1 && current_infrared_right_state == 0) {
        set_rgb_led(led_red_right, led_green_right, led_blue_right, 0, 0, 0);
        set_rgb_led(led_red_left, led_green_left, led_blue_left, 17, 236, 229);
        stop_motors();
      }
      if (current_infrared_right_state == 0 && current_infrared_left_state == 0) {
        set_rgb_led(led_red_right, led_green_right, led_blue_right, 0, 0, 0);
        set_rgb_led(led_red_left, led_green_left, led_blue_left, 0, 0, 0);
        stop_motors();
      }
      if (current_infrared_left_state == 1 && current_infrared_right_state == 1) {
        set_rgb_led(led_red_right, led_green_right, led_blue_right, 0, 0, 0);
        set_rgb_led(led_red_left, led_green_left, led_blue_left, 0, 0, 0);
        stop_motors();
      }
    }

    if (distance_cm > 5 && distance_cm < 20) {
      pwm_value = map_user_input(255);
      set_rgb_led(led_red_right, led_green_right, led_blue_right, 0, pwm_value, 0);
      set_rgb_led(led_red_left, led_green_left, led_blue_left, 0, pwm_value, 0);
      forward();
    } else if (distance_cm > 20 && distance_cm < 40) {
      pwm_value = map_user_input(255);
      set_rgb_led(led_red_right, led_green_right, led_blue_right, pwm_value, 0, 0);
      set_rgb_led(led_red_left, led_green_left, led_blue_left, pwm_value, 0, 0);
      backward();
    }
  } catch (...) {
    Serial.println("Invalid input. Please enter a valid number.");
  }
}

int get_distance() {
  // Implement the ultrasonic distance measurement logic here
}

void set_rgb_led(int red_pin, int green_pin, int blue_pin, int r_value, int g_value, int b_value) {
  analogWrite(red_pin, r_value);
  analogWrite(green_pin, g_value);
  analogWrite(blue_pin, b_value);
}

void stop_motors() {
  analogWrite(motor1_pwm_pin, 0);
  analogWrite(motor2_pwm_pin, 0);
}

void forward() {
  digitalWrite(motor1_dir_pin, HIGH);
  digitalWrite(motor2_dir_pin, HIGH);
  analogWrite(motor1_pwm_pin, speed_pwm);
  analogWrite(motor2_pwm_pin, speed_pwm);
}
int get_distance() {
  // Trigger pulse to start measurement
  digitalWrite(trigger_pin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigger_pin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigger_pin, LOW);

  // Measure the pulse width on the echo pin
  long pulse_width = pulseIn(echo_pin, HIGH, 30000);  // 30ms timeout (max range)

  // Calculate distance in centimeters
  int distance = pulse_width / 58;

  return distance;
}

void backward() {
  digitalWrite(motor1_dir_pin, LOW);
  digitalWrite(motor2_dir_pin, LOW);
  analogWrite(motor1_pwm_pin, speed_pwm);
  analogWrite(motor2_pwm_pin, speed_pwm);
}

int map_user_input(int user_input) {
  // Ensure user_input is within the valid range
  user_input = max(0, min(255, user_input));
  // Map the value to the PWM range
  return int((user_input / 255.0) * 65535.0);
}

int map_speed_to_pwm(int speed) {
  // Ensure speed is within the valid range
  speed = max(0, min(100, speed));
  // Map the speed to the PWM range
  return int((speed / 100.0) * 65535.0);
}

