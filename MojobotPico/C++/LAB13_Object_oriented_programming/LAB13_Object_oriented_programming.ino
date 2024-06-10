#include <Arduino.h>

// UltrasonicSensor Class
class UltrasonicSensor {
private:
    int triggerPin;
    int echoPin;

public:
    UltrasonicSensor(int trigPin, int echoPin) {
        this->triggerPin = trigPin;
        this->echoPin = echoPin;
        pinMode(triggerPin, OUTPUT);
        pinMode(echoPin, INPUT);
    }

    long measureDistance() {
        digitalWrite(triggerPin, LOW);
        delayMicroseconds(2);
        digitalWrite(triggerPin, HIGH);
        delayMicroseconds(10);
        digitalWrite(triggerPin, LOW);
        long duration = pulseIn(echoPin, HIGH);
        long distance_cm = duration * 0.034 / 2;
        return distance_cm;
    }
};

// LineFollowerSensor Class
class LineFollowerSensor {
private:
    int leftSensorPin;
    int rightSensorPin;

public:
    LineFollowerSensor(int leftPin, int rightPin) {
        this->leftSensorPin = leftPin;
        this->rightSensorPin = rightPin;
        pinMode(leftPin, INPUT);
        pinMode(rightPin, INPUT);
    }

    int getTrackingState() {
        int leftSensor = digitalRead(leftSensorPin);
        int rightSensor = digitalRead(rightSensorPin);

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
};

// Motor Class
class Motor {
private:
    int pwmPin;
    int dirPin;

public:
    Motor(int pwm, int dir) {
        this->pwmPin = pwm;
        this->dirPin = dir;
        pinMode(pwm, OUTPUT);
        pinMode(dir, OUTPUT);
    }

    void setSpeed(int speed) {
        if (speed > 0) {
            digitalWrite(dirPin, HIGH);
        } else {
            digitalWrite(dirPin, LOW);
        }

        speed = abs(speed);
        speed = constrain(speed, 0, 100);
        int pwmValue = map(speed, 0, 100, 0, 255);
        analogWrite(pwmPin, pwmValue);
    }
};

// Robot Class
class Robot {
private:
    UltrasonicSensor ultrasonicSensor;
    LineFollowerSensor lineFollowerSensor;
    Motor leftMotor;
    Motor rightMotor;
    int ledPinLeft;
    int ledPinRight;

public:
    Robot(UltrasonicSensor us, LineFollowerSensor lfs, Motor lm, Motor rm, int ledLeft, int ledRight)
        : ultrasonicSensor(us), lineFollowerSensor(lfs), leftMotor(lm), rightMotor(rm), ledPinLeft(ledLeft), ledPinRight(ledRight) {
        pinMode(ledLeft, OUTPUT);
        pinMode(ledRight, OUTPUT);
    }

    int generateRandom20() {
        randomSeed(analogRead(0)); // You can use any analog pin for seeding
        return random(2) ? -20 : 20;
    }

    void execute() {
        int trackingState = lineFollowerSensor.getTrackingState();
        long distance_cm = ultrasonicSensor.measureDistance();

        if (distance_cm > 3) {
            if (trackingState == 0) {
                digitalWrite(ledPinLeft, LOW);
                digitalWrite(ledPinRight, LOW);
                int speed = generateRandom20();
                leftMotor.setSpeed(speed);
                rightMotor.setSpeed(-speed);
                delay(200);
            } else if (trackingState == 1) {
                digitalWrite(ledPinLeft, HIGH);
                digitalWrite(ledPinRight, LOW);
                leftMotor.setSpeed(30);
                rightMotor.setSpeed(-30);
            } else if (trackingState == 10) {
                digitalWrite(ledPinLeft, LOW);
                digitalWrite(ledPinRight, HIGH);
                leftMotor.setSpeed(-30);
                rightMotor.setSpeed(30);
            } else if (trackingState == 11) {
                digitalWrite(ledPinLeft, HIGH);
                digitalWrite(ledPinRight, HIGH);
                leftMotor.setSpeed(30);
                rightMotor.setSpeed(30);
            }
        } else {
            digitalWrite(ledPinLeft, HIGH);
            digitalWrite(ledPinRight, HIGH);
            leftMotor.setSpeed(0);
            rightMotor.setSpeed(0);
        }
        delay(100);
    }
};

// Pin Definitions
const int TRIGGER_PIN = 14;
const int ECHO_PIN = 15;
const int LEFT_SENSOR_PIN = 3;
const int RIGHT_SENSOR_PIN = 2;
const int MOTOR1_PWM_PIN = 10;
const int MOTOR1_DIR_PIN = 12;
const int MOTOR2_PWM_PIN = 11;
const int MOTOR2_DIR_PIN = 13;
const int LED_PIN_LEFT = 22;
const int LED_PIN_RIGHT = 7;

// Instantiate Components
UltrasonicSensor ultrasonicSensor(TRIGGER_PIN, ECHO_PIN);
LineFollowerSensor lineFollowerSensor(LEFT_SENSOR_PIN, RIGHT_SENSOR_PIN);
Motor leftMotor(MOTOR1_PWM_PIN, MOTOR1_DIR_PIN);
Motor rightMotor(MOTOR2_PWM_PIN, MOTOR2_DIR_PIN);
Robot robot(ultrasonicSensor, lineFollowerSensor, leftMotor, rightMotor, LED_PIN_LEFT, LED_PIN_RIGHT);

void setup() {
    Serial.begin(115200);
}

void loop() {
    robot.execute();
}
