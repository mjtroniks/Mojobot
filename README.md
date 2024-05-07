# Mojobot by MJtronics
 ![alt text](https://github.com/mjtroniks/Mojobot/blob/4d80b0dbb44b8dbe23df34b33c5dae10a4e39261/MojobotPico/Micropython/Images/Assembly.PNG)
## Introduction

Mojobot by MJtronics is an innovative robot designed for educational purposes and hobbyist projects, providing a versatile platform for learning and experimentation. 
## Get started

- **[Micropython:]**(https://github.com/mjtroniks/Mojobot/wiki/Introduction-and-Blink-program) Visit our [Wiki](https://github.com/mjtroniks/Mojobot/wiki) to access all topics.
- **C++:** Under development
- **Makecode:** Under development

## Characteristics

- **Motors:** Rear-drive high-speed GA12-N20 DC micro gear deceleration motors.
- **Assembly:** Battery holder, batteries and Raspberry Pi Pico. Very simple assembly :)

## Robot Specs

- **Voltage:** 3.5V to 5V.
- **Dimension:** 84mm x 84mm x 40mm.
- **Motor Type:** GA12-N20 DC micro gear deceleration motors (300 RPM).
- **Ultrasonic Sensor:** HC-SR04 (2cm to 400cm range).
- **RGB Headlights:** Two RGB LEDs.
- **Infrared Control:** Two infrared sensors for line detection.
- **Microcontroller:** Supports Raspberry pico and Raspberry pico W.


### Components List (Included):

- 1 x Mojobot car
- 1 x Battery Holder
- 1 x HC-SR04 Ultrasonic Sensor
- 1 x Raspberry Pi Pico
- 1 x MPU6050

### Pins Description

**Motors:**

- Motor 1 PWM (GP10) - Controls the speed of Motor 1.
- Motor 1 Direction (GP12) - Controls the direction of Motor 1.
- Motor 2 PWM (GP11) - Controls the speed of Motor 2.
- Motor 2 Direction (GP13) - Controls the direction of Motor 2.

**Ultrasonic Sensor:**

- Trigger (GP14) - Initiates ultrasonic distance measurement.
- Echo (GP15) - Measures the duration of the ultrasonic pulse.

**RGB Headlights:**

- Right LED (GP22, GP21, GP20) - RGB pins for the right LED.
- Left LED (GP7, GP8, GP9) - RGB pins for the left LED.

**Infrared Control:**

- Left Infrared Sensor (GP2) - Input pin for the left infrared sensor.
- Right Infrared Sensor (GP3) - Input pin for the right infrared sensor.

**MPU6050:**

- SCL GP19
- SDA GP18

### Unused Pins (Pico):

**Used Pins:** GP2, GP3, GP7, GP8, GP9, GP10, GP11, GP12, GP13, GP14, GP15, GP20, GP21, GP22.

**Unused Available GPIO Pins:** GP0, GP1, GP4, GP5, GP6, GP16, GP17, GP26, GP27, GP28, GP29.

## Applications

Mojobot is ideal for educational purposes, allowing users to explore robotics, sensor integration, and programming. It serves as a great platform for learning about motor control, ultrasonic sensing, and infrared communication.

Mojobot is a versatile and user-friendly robot that encourages creativity and experimentation in the field of robotics.
