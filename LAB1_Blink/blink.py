"""
*****************************
* Developer: MJtronics
* Date: 2024-01-15
*****************************

Description:
This code controls an LED using the machine module on a microcontroller.
The LED is intended to blink on and off repeatedly, with each state lasting
for 0.5 seconds, creating a visible blinking effect.

Expected Results:
- The LED should turn on for 0.5 seconds.
- Then, the LED should turn off for 0.5 seconds.
- This on-off cycle should repeat indefinitely.

"""

import machine
from time import *

# Define the LED pin
led = machine.Pin("LED", machine.Pin.OUT)

# Main loop to toggle the LED
while True:
    # Turn on the LED
    led.on()

    # Pause for 0.5 seconds
    sleep(0.5)

    # Turn off the LED
    led.off()

    # Pause for 0.5 seconds
    sleep(0.5)
