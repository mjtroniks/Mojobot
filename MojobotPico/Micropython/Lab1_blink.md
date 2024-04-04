# Blink Onboard LED

## Introduction

The Raspberry Pi Pico is a low-cost microcontroller board developed by the Raspberry Pi Foundation.

## Key Features:

Microcontroller: Powered by the RP2040 chip, featuring a dual-core ARM Cortex-M0+ processor running at up to 133MHz.

Connectivity: Offers 26 multifunction GPIO pins, USB 1.1 support, UART, SPI, and I2C interfaces.

Memory: Equipped with 264KB of embedded SRAM and 2MB of external flash memory.

Low Power: Designed for energy efficiency, suitable for battery-powered applications and IoT devices.

Development Environment: Supported by MicroPython, C/C++, and CircuitPython for firmware development.





![MicroController](https://github.com/mjtroniks/Mojobot/blob/d91b9694c7622a41186362987df0de14fe8cf188/MojobotPico/Micropython/Images/Raspberry-Pi-PICO-Pinout-Diagram.jpeg)

## Overview

This tutorial is a quick guide to blinking the onboard LED using a Raspberry Pi Pico microcontroller. 

1. Make sure Python 3 or above has been installed on your computer as described in LAB0_IDE Setup
   You can verify Python is installed by typing CMD in the search box next to the Windows logo
   
    ![CMD](https://github.com/mjtroniks/Mojobot/assets/91319956/02b7292a-49ee-4ba3-920f-b8da121474a0)
   

   Then type python --version as in the picture below
    
    ![python verification_LI](https://github.com/mjtroniks/Mojobot/assets/91319956/4fcb745d-56cd-485c-ae5f-e6ecd9254859)
   If the python version is displayed you are ready to go. Otherwise proceed to Lab0_IDE Setup Instructions

3. Connect Raspberry Pi Pico to your Computer: Use a USB cable to connect your Raspberry Pi Pico to your computer.

4. Make sure Pycharm IDE is Installed and configured as in LAB0_IDE Setup

5. Create a project and make sure create main.py is selected

![Create new project](https://github.com/mjtroniks/Mojobot/assets/91319956/465d9c90-44bc-4e4b-89c8-d8ddb3b7082d)

5. Install Micropython plugin by Clicking File => Settings => Plugins
 You will be asked to restart the Pycharm IDE. Click on restart.
   ![plugins](https://github.com/mjtroniks/Mojobot/assets/91319956/3e8270cd-9e98-4446-b13d-6ac5d24681b3)
   
6. Enable micropython support by clicking on File => Settings => Language and frameworks
     ![uPython](https://github.com/mjtroniks/Mojobot/assets/91319956/8dad115b-7f8a-4a62-9f97-2b02803d9563)

7. Select Raspberry pico from the drop down list and click okay to close the window
   ![Enable Raspberry pico support](https://github.com/mjtroniks/Mojobot/assets/91319956/bc012dd5-a74d-40b4-81e3-ab16f3814af1)

8. Click on the blue message to install the Raspberry pico libraries
   
![Install pico libraries](https://github.com/mjtroniks/Mojobot/assets/91319956/4afc2357-91ee-4ed1-ba7e-02b28793df8d)

9. Paste the following code on the main file
    ![Downloading Examples](https://github.com/mjtroniks/Mojobot/assets/91319956/a793520d-d099-4fe4-8bf9-e2bdad74fefe)
```python
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


11. Run the code by clicking on Run => Run Flash

 
![Screenshot (5)](https://github.com/mjtroniks/Mojobot/assets/91319956/2d5ea12d-c6b4-4eed-b0b7-bd88c9130730)


12. The output should be displayed as in the video below

https://github.com/mjtroniks/Mojobot/assets/91319956/337c32e1-be6a-4129-96bc-3f552dda97c5
