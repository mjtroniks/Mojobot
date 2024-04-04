# Blink External LED

## Introduction

The Raspberry Pi Pico is a low-cost microcontroller board developed by the Raspberry Pi Foundation.

## Key Features:

Microcontroller: Powered by the RP2040 chip, featuring a dual-core ARM Cortex-M0+ processor running at up to 133MHz.

Connectivity: Offers 26 multifunction GPIO pins, USB 1.1 support, UART, SPI, and I2C interfaces.

Memory: Equipped with 264KB of embedded SRAM and 2MB of external flash memory.

Low Power: Designed for energy efficiency, suitable for battery-powered applications and IoT devices.

Development Environment: Supported by MicroPython, C/C++, and CircuitPython for firmware development.

## Capabilities:

Versatile I/O: GPIO pins support digital/analog I/O, PWM output, and communication with external devices.

Real-Time Performance: Dual-core processor and high clock speed enable real-time processing.

Expandability: Easily expandable with additional hardware components for various projects.

Low-Cost: Affordable pricing and extensive software support make it accessible for hobbyists and professionals.

Community Support: Benefits from a large and active community for resources, tutorials, and projects.

![MicroController](https://github.com/mjtroniks/Mojobot/blob/d91b9694c7622a41186362987df0de14fe8cf188/MojobotPico/Micropython/Images/Raspberry-Pi-PICO-Pinout-Diagram.jpeg)

## Overview

This tutorial is a quick guide to blinking an external LED using a Raspberry Pi Pico microcontroller. The experiment can be simulated or implemented practically.

![Single led](https://github.com/mjtroniks/Mojobot/blob/187de62fef51af3a482342244b06f739f5f322e9/MojobotPico/Micropython/Images/pico.mp4)

## Instructions

The robot left LED are wired as in the following diagram:

![Single led](https://github.com/mjtroniks/Mojobot/blob/d91b9694c7622a41186362987df0de14fe8cf188/MojobotPico/Micropython/Images/Single%20led_bb.jpg)

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

![Robot Leds](https://github.com/mjtroniks/Mojobot/blob/dcf25ff05e4eff7f64864f8ec74484e06fddeac2/MojobotPico/Micropython/Images/left%20right%20led.PNG)

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


