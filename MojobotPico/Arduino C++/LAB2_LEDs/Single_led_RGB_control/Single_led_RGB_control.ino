//*****************************
//* Developer: MJtronics
//* Date: 2024-01-15
//*****************************

// Description:
// This C++ code demonstrates PWM (Pulse Width Modulation) on a Raspberry Pi MojobotPico.
// It allows the user to interactively control the brightness of an LED connected to pin GP22.
// The code gradually increases and decreases the duty cycle of the LED, creating a smooth fading effect.
// User input is utilized to set the desired brightness level.

// Pin Configuration:
// LEDL (Left LED)
// - R: GP22
// - B: GP21
// - G: GP20

// LEDR (Right LED)
// - R: GP7
// - B: GP8
// - G: GP9

#include <Arduino.h>

// Pin connected to the LED
const int ledPin = 22;

// Time interval between brightness steps (in milliseconds)
const int fadeInterval = 10;

// Maximum and minimum brightness values
const int maxBrightness = 255; // This can be changed to 65535 if the below settings are uncommented
const int minBrightness = 0;

// Current brightness value
int brightness = minBrightness;

// Direction flag for fading (true = increasing, false = decreasing)
bool fadingDirection = true;

void setup() {
  // Initialize the LED pin as an output
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
  Serial.println("Enter the desired brightness level (0-255): ");
  // Adjust PWM properties if needed
  /*analogWriteFreq(5000);
  analogWriteRange(65535);
  analogWriteResolution(16);*/
  // Prompt the user to input the level of brightness

}

void loop() {
  // Prompt the user to input the level of brightness
  Serial.println("Enter the desired brightness level (0-255): ");

  // Wait for user input
  while (Serial.available() == 0) {
    delay(10);
  }

  // Read user input
  int userBrightness = Serial.parseInt();

  // Map user input to PWM range
  brightness = max(min(userBrightness, 255), 0);

  // Set the LED brightness
  analogWrite(ledPin, brightness);

  // Clear any remaining characters in the input buffer
  while (Serial.available() > 0) {
    Serial.read();
  }
}
