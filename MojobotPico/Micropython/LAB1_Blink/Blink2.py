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
ledRR = machine.Pin(7, machine.Pin.OUT)
ledGR = machine.Pin(9, machine.Pin.OUT)
ledBR = machine.Pin(8, machine.Pin.OUT)
ledRL = machine.Pin(22, machine.Pin.OUT)
ledBL = machine.Pin(20, machine.Pin.OUT)
ledGL = machine.Pin(21, machine.Pin.OUT)
# Main loop to toggle the LED
while True:
    # Turn on the LED
    ledRR.off()#pin7
    ledBR.off()#pin9
    ledGR.off()#pin8
    ledRL.off()#pin7
    ledBL.off()#pin20
    ledGL.off()#pin21
    # Pause for 0.5 seconds
    sleep(0.5)

    # Turn off the LED
    ledRR.off()
    ledBR.off()
    ledGR.off()
    ledRL.off()
    ledBL.off()
    ledGL.off()
    # Pause for 0.5 seconds
    sleep(0.5)
