//*****************************
//* Developer: MJtronics
//* Date: 2024-01-15
//*****************************

// Description:
// This code controls two RGB LEDs using PWM signals on a microcontroller.
// It prompts the user for LED brightness input (0-255) and displays
// alternating colors on the right and left RGB LEDs.

// Expected Results:
// - The RGB LEDs will display alternating green and red colors with the specified brightness.
// - Each color will be displayed for a duration of 3 seconds, with a 3-second pause between actions.

#include <Arduino.h>

// Pin configuration for RGB LEDs
const int redPinRight = 7;
const int greenPinRight = 8;
const int bluePinRight = 9;
const int redPinLeft = 22;
const int greenPinLeft = 21;
const int bluePinLeft = 20;

void setup() {
    Serial.begin(9600);
    pinMode(redPinRight, OUTPUT);
    pinMode(greenPinRight, OUTPUT);
    pinMode(bluePinRight, OUTPUT);
    pinMode(redPinLeft, OUTPUT);
    pinMode(greenPinLeft, OUTPUT);
    pinMode(bluePinLeft, OUTPUT);
}

// Function to map user input (0-255) to PWM range (0-255)
int mapUserInput(int userInput) {
    userInput = max(0, min(255, userInput));
    return int((userInput / 255.0) * 255);
}

// Function to set RGB LED colors
void setRgbLedColor(int redPin, int greenPin, int bluePin, int rValue, int gValue, int bValue) {
    analogWrite(redPin, rValue);
    analogWrite(greenPin, gValue);
    analogWrite(bluePin, bValue);
}

void loop() {
    if (Serial.available() > 0) {
        Serial.print("Enter a brightness value (0-255): ");
        while (Serial.available() == 0) {}
        int brightness = Serial.parseInt();
        int mappedValue = mapUserInput(brightness);

        setRgbLedColor(redPinRight, greenPinRight, bluePinRight, mappedValue, 0, 0);
        setRgbLedColor(redPinLeft, greenPinLeft, bluePinLeft, 0, mappedValue, 0);
        delay(3000);

        setRgbLedColor(redPinRight, greenPinRight, bluePinRight, 0, mappedValue, 0);
        setRgbLedColor(redPinLeft, greenPinLeft, bluePinLeft, mappedValue, 0, 0);
        delay(3000);
    }
}
