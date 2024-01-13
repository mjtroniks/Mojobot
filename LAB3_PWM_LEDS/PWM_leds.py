import machine
led = machine.Pin("LED", machine.Pin.OUT)
led.on()
from machine import Pin, PWM
from time import sleep

# Set up PWM Pins for RGB Left (GP28, GP27, GP26)
led_r = Pin(28)
led_g = Pin(27)
led_b = Pin(26)

pwm_r = PWM(led_r)
pwm_g = PWM(led_g)
pwm_b = PWM(led_b)

# Set PWM frequency for RGB Left
frequency = 5000
pwm_r.freq(frequency)
pwm_g.freq(frequency)
pwm_b.freq(frequency)

# Set up PWM Pins for RGBR (GP19, GP20, GP22)
led_r_r = Pin(7)
led_g_r = Pin(8)
led_b_r = Pin(9)

pwm_r_r = PWM(led_r_r)
pwm_g_r = PWM(led_g_r)
pwm_b_r = PWM(led_b_r)

# Set PWM frequency for RGBR
pwm_r_r.freq(frequency)
pwm_g_r.freq(frequency)
pwm_b_r.freq(frequency)

duty_step = 129  # Step size for changing the duty cycle

while True:
    # Increase the duty cycle gradually for RGB Left
    for duty_cycle in range(0, 65536, duty_step):
        pwm_r.duty_u16(duty_cycle)
        pwm_g.duty_u16(duty_cycle)
        pwm_b.duty_u16(duty_cycle)
        pwm_r_r.duty_u16(duty_cycle)
        pwm_g_r.duty_u16(duty_cycle)
        pwm_b_r.duty_u16(duty_cycle)
        sleep(0.005)

    # Decrease the duty cycle gradually for RGB Left
    for duty_cycle in range(65536, 0, -duty_step):
        pwm_r.duty_u16(duty_cycle)
        pwm_g.duty_u16(duty_cycle)
        pwm_b.duty_u16(duty_cycle)
        pwm_r_r.duty_u16(duty_cycle)
        pwm_g_r.duty_u16(duty_cycle)
        pwm_b_r.duty_u16(duty_cycle)
        sleep(0.005)
