// Define the LED pin
const int LED_PIN = 21; // Onboard LED of the Raspberry Pi Pico
const int LED_PIN2 = 8; // Onboard LED of the Raspberry Pi Pico
void setup() {
  // Initialize the LED pin as an output
  pinMode(LED_PIN, OUTPUT);
  pinMode(LED_PIN2, OUTPUT);
}

void loop() {
  // Turn the LED on
  digitalWrite(LED_PIN, HIGH);
  digitalWrite(LED_PIN2, HIGH);
  // Wait for a second
  delay(1000);
  // Turn the LED off
  digitalWrite(LED_PIN, LOW);
  digitalWrite(LED_PIN2, LOW);
  // Wait for a second
  delay(1000);
}