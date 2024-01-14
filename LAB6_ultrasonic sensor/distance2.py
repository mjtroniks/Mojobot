from machine import Pin, time_pulse_us
import utime

# Ultrasonic sensor pins
trigger_pin = Pin(14, Pin.OUT)
echo_pin = Pin(15, Pin.IN)

def measure_distance():
    # Trigger pulse to start measurement
    trigger_pin.off()
    utime.sleep_us(2)
    trigger_pin.on()
    utime.sleep_us(10)
    trigger_pin.off()

    # Measure the pulse width on the echo pin
    pulse_width = time_pulse_us(echo_pin, 1, 30000)  # 30ms timeout (max range)

    # Calculate distance in centimeters
    distance_cm = (pulse_width / 2) / 29.1

    return distance_cm

try:
    while True:
        distance = measure_distance()
        utime.sleep_ms(100) # to avoid measuring to frequently
        print("Distance:", distance, "cm")


except KeyboardInterrupt:
    print("Measurement stopped by user")
