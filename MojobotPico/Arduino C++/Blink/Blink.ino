//*****************************
//* Developer: MJtronics
//* Date: 2024-01-15
//*****************************

// Description:
// This code controls an LED using the Arduino framework on a Raspberry Pi Pico.
// The LED is intended to blink on and off repeatedly, with each state lasting
// for 0.5 seconds, creating a visible blinking effect.

// Define the LED pin
#define ledPin LED_BUILTIN

void setup() {
  // Set the LED pin as an output
  pinMode(ledPin, OUTPUT);
}

void loop() {
  // Turn on the LED
  digitalWrite(ledPin, HIGH);

  // Pause for 0.5 seconds
  delay(500);

  // Turn off the LED
  digitalWrite(ledPin, LOW);

  // Pause for 0.5 seconds
  delay(500);
}
