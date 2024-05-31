#include <Arduino.h>
#include "pico/multicore.h"

const uint LEFT_LED_PIN = 21;
const uint RIGHT_LED_PIN = 8;

void blink_left_led()
{
    while (true)
    {
        digitalWrite(LEFT_LED_PIN, HIGH);
        delay(500);
        digitalWrite(LEFT_LED_PIN, LOW);
        delay(500);
    }
}

void blink_right_led()
{
    while (true)
    {
        digitalWrite(RIGHT_LED_PIN, HIGH);
        delay(500);
        digitalWrite(RIGHT_LED_PIN, LOW);
        delay(500);
    }
}

// Function to be run on core 1
void core1_entry()
{
    pinMode(RIGHT_LED_PIN, OUTPUT);
    blink_right_led();
}

// Running on Core0
void setup()
{
    Serial.begin(115200);
    while (!Serial);
    Serial.println("Start RPI_Pico_Multicore Core0");

    pinMode(LEFT_LED_PIN, OUTPUT);

    // Launch core 1
    multicore_launch_core1(core1_entry);
}

void loop()
{
    blink_left_led();
}
