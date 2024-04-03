# Blink External LED

## Overview

This tutorial is a quick guide to blinking an external LED using a Raspberry Pi Pico microcontroller.

## Instructions

Grab a BLUE LED or any LED rated for 3 volts. Insert the long pin into column 30 and the short pin into column 31 on the breadboard.

Connect the short side of the LED to the ground/negative rail of the breadboard. Then, connect the long side of the LED to column 20, corresponding to the GP16 pin of the Raspberry Pi Pico.

![Blink Diagram](/images/7_blink_external_bb.png)

After setting up the LED, let's write the code. We'll use the following code snippet, which is similar to what we've used before but with the Pin number changed from the onboard LED pin 25 to the GP16 pin.

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


