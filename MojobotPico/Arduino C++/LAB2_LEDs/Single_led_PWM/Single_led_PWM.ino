//*****************************
//* Developer: MJtronics
//* Date: 2024-01-15
//*****************************

// Description:
// This C++ code demonstrates PWM (Pulse Width Modulation) on a Raspberry Pi MojobotPico.
// It gradually increases and decreases the duty cycle of an LED connected to pin GP22, creating
// a smooth fading effect.

// Pin Configuration:
// LEDL (Left LED)
// - R: GP22
// - B: GP21
// - G: GP20

// LEDR (Right LED)
// - R: GP7
// - B: GP8
// - G: GP9

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
  pinMode(ledPin, OUTPUT);
  // Adjust PWM properties if needed
  /*analogWriteFreq(5000);
  analogWriteRange(65535);
  analogWriteResolution(16);*/
}

void loop() {
  // Update the brightness value based on the fading direction
  if (fadingDirection) {
    for (int i = brightness; i <= maxBrightness; i++) {
      brightness = i;
      Serial.println(brightness);
      
      // Set the LED brightness
      analogWrite(ledPin, brightness);
      
      // Delay for the fade interval
      delay(fadeInterval);
    }
    
    fadingDirection = false;
  } else {
    for (int i = brightness; i >= minBrightness; i--) {
      brightness = i;
      Serial.println(brightness);
      
      // Set the LED brightness
      analogWrite(ledPin, brightness);
      
      // Delay for the fade interval
      delay(fadeInterval);
    }
    
    fadingDirection = true;
  }
}
