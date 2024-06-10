// Pin definitions for RGB LED
const int redPin = 7;
const int greenPin = 8;
const int bluePin = 9;

// Define variables for color intensity
int redIntensity = 255;     // Max intensity for red (0 to 255)
int greenIntensity = 128;   // Medium intensity for green (0 to 255)
int blueIntensity = 0;      // No intensity for blue (0 to 255)

void setup() {
  // Initialize serial communication at 9600 bits per second
  Serial.begin(9600);

  // Initialize the LED pins as outputs
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
}

void loop() {
  // Apply color to RGB LED using variables
  analogWrite(redPin, redIntensity);     // Set red intensity
  analogWrite(greenPin, greenIntensity); // Set green intensity
  analogWrite(bluePin, blueIntensity);   // Set blue intensity

  // Wait for a while
  delay(5000);

  // Change color intensity
  redIntensity = 0;
  greenIntensity = 255;
  blueIntensity = 255;

  // Apply new color to RGB LED
  analogWrite(redPin, redIntensity);
  analogWrite(greenPin, greenIntensity);
  analogWrite(bluePin, blueIntensity);

  // Wait for a while
  delay(5000);

  // Turn off the LED
  analogWrite(redPin, 0);
  analogWrite(greenPin, 0);
  analogWrite(bluePin, 0);
}
