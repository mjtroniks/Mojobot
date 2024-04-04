# Blink External LED

## Overview

This tutorial is a quick guide to blinking an external LED using a Raspberry Pi Pico microcontroller.

## Instructions

The robot LEDs are wired as in the following diagram:

![Blink Diagram](https://github.com/mjtroniks/Mojobot/blob/4445f12cad92337dabb1a75218ab8db92b7634c7/MojobotPico/Micropython/Images/LED%20setup%20breadboard.jpg)

Left LED Connections:

Red (R): Connect the leg adjacent to the flat side of the LED to a 330 ohm resistor. Connect the other side of the resistor to GPIO pin 7 on the Raspberry Pi Pico. This pin regulates the intensity of the red color.
Ground: Link the next leg after the red leg directly to the ground (GND) on the Raspberry Pi Pico.
Blue (B): Attach the leg succeeding the ground connection to a 330 ohm resistor. Connect the other side of the resistor to GPIO pin 9 on the Raspberry Pi Pico. This pin controls the intensity of the blue color.
Green (G): Link the leg succeeding the blue leg to a 330 ohm resistor. Connect the other side of the resistor to GPIO pin 8 on the Raspberry Pi Pico. This pin manages the intensity of the green color.
Right LED Connections:

Red (R): Connect the leg adjacent to the flat side of the LED to a 330 ohm resistor. Link the other side of the resistor to GPIO pin 22 on the Raspberry Pi Pico.
Green (G): Attach the leg succeeding the red leg to a 330 ohm resistor. Connect the other side of the resistor to GPIO pin 21 on the Raspberry Pi Pico.
Blue (B): Link the leg succeeding the green leg to a 330 ohm resistor. Connect the other side of the resistor to GPIO pin 20 on the Raspberry Pi Pico.
This arrangement ensures that each color leg of the LED is connected through a 330 ohm resistor to manage the current flow, allowing for independent control of the intensity of each color (red, green, and blue) for both the left and right LEDs.

![Robot Leds](https://github.com/mjtroniks/Mojobot/blob/cd53ea3b82a8e93e5dd9dff7ae1ecf58c41ba8f0/MojobotPico/Micropython/Images/LEDs%20on%20robot.PNG)

After setting up the LEDs, let's write the code. 



```python
from machine import Pin
import utime

led = Pin(16, Pin.OUT)

while True:
    led.toggle()
    utime.sleep_ms(1000)

## Other Pin Functions

Another approach to control the LED's state is by utilizing the [value() function](https://docs.micropython.org/en/latest/library/machine.Pin.html#machine.Pin.value).

Below is the code snippet demonstrating this method:

```python
from machine import Pin
import utime

led = Pin(16, Pin.OUT)

while True:
    led.value(1)
    utime.sleep_ms(1000)
    led.value(0)
    utime.sleep_ms(1000)


