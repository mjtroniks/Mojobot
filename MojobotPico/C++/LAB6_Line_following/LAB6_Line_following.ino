#include <Arduino.h>

// Sensor pins
const int leftSensorPin = 3;
const int rightSensorPin = 2;

// LED pins
const int leftLedPin = 22;
const int rightLedPin = 7;

const int blueRPin = 9;
const int blueLPin = 20;

void setup() {
    pinMode(leftSensorPin, INPUT);
    pinMode(rightSensorPin, INPUT);
    pinMode(leftLedPin, OUTPUT);
    pinMode(rightLedPin, OUTPUT);
    pinMode(blueRPin, OUTPUT);
    pinMode(blueLPin, OUTPUT);
    Serial.begin(9600);
}

int getTracking() {
    int left = digitalRead(leftSensorPin);
    int right = digitalRead(rightSensorPin);

    if (left == 0 && right == 0) {
        return 0;
    } else if (left == 0 && right == 1) {
        return 1;
    } else if (left == 1 && right == 0) {
        return 10;
    } else if (left == 1 && right == 1) {
        return 11;
    }
    return -1; // Fallback case
}

void loop() {
    int trackingState = getTracking();

    if (trackingState == 0) {
        Serial.println("Both sensor on a white reflective surface");
        digitalWrite(leftLedPin, LOW);
        digitalWrite(rightLedPin, LOW);
        digitalWrite(blueRPin, HIGH);
        digitalWrite(blueLPin, HIGH);

    } else if (trackingState == 1) {
        Serial.println("Right triggered");
        // Call to motor control function to adjust speed, e.g., motorsSpeed(30, 5);
        digitalWrite(leftLedPin, LOW);
        digitalWrite(rightLedPin, HIGH);
        digitalWrite(blueRPin, LOW);
        digitalWrite(blueLPin, LOW);

    } else if (trackingState == 10) {
        Serial.println("Left triggered");
        // Call to motor control function to adjust speed, e.g., motorsSpeed(5, 30);
        digitalWrite(leftLedPin, HIGH);
        digitalWrite(rightLedPin, LOW);
        digitalWrite(blueRPin, LOW);
        digitalWrite(blueLPin, LOW);

    } else if (trackingState == 11) {
        Serial.println("Line detected");
        digitalWrite(leftLedPin, HIGH);
        digitalWrite(rightLedPin, HIGH);
        digitalWrite(blueRPin, LOW);
        digitalWrite(blueLPin, LOW);
    }

    delay(100); // Adjust the delay as necessary
}