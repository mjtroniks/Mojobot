#include <Arduino.h>

// Global variable declaration
int distance_cm = 0;  // Global variable

void measure_distance() {
    distance_cm = 10;  // Modify the global variable
    Serial.print("Inside measure_distance, distance_cm: ");
    Serial.println(distance_cm);
}

void another_function() {
    distance_cm = 20;  // Modify the global variable
    Serial.print("Inside another_function, distance_cm: ");
    Serial.println(distance_cm);
}

void local_variable_example() {
    int local_distance = 5;  // Local variable
    int distance_cm = 1;  // Local variable, does not affect the global distance_cm
    Serial.print("Inside local_variable_example, local_distance: ");
    Serial.println(local_distance);
    Serial.print("Inside local_variable_example, distance_cm: ");
    Serial.println(distance_cm);
}

void setup() {
    // Initialize serial communication
    Serial.begin(9600);
    delay(8000);

    // Initial value of global variable
    Serial.print("Initial global distance_cm: ");
    Serial.println(distance_cm);

    // Call the functions
    measure_distance();
    Serial.print("Global distance_cm after measure_distance: ");
    Serial.println(distance_cm);

    another_function();
    Serial.print("Global distance_cm after another_function: ");
    Serial.println(distance_cm);

    local_variable_example();
    Serial.print("Global distance_cm after local_variable_example: ");
    Serial.println(distance_cm);  // Confirm it hasn't changed
}

void loop() {
    // Put your main code here, to run repeatedly:
}