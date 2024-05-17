// Define the LED pin
const int LED_PIN = 22; // Onboard LED of the Raspberry Pi Pico

void setup() {
  // Initialize the LED pin as an output
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  // Turn the LED on
  digitalWrite(LED_PIN, HIGH);
  // Wait for a second
  delay(1000);
  // Turn the LED off
  digitalWrite(LED_PIN, LOW);
  // Wait for a second
  delay(1000);
}
