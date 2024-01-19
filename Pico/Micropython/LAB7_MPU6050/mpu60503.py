from machine import Pin, I2C
import utime
import math

PWR_MGMT_1 = 0x6B
SMPLRT_DIV = 0x19
CONFIG = 0x1A
GYRO_CONFIG = 0x1B
ACCEL_CONFIG = 0x1C
TEMP_OUT_H = 0x41
ACCEL_XOUT_H = 0x3B
GYRO_XOUT_H = 0x43


def init_mpu6050(i2c, address=0x68):
    i2c.writeto_mem(address, PWR_MGMT_1, b'\x00')
    utime.sleep_ms(100)
    i2c.writeto_mem(address, SMPLRT_DIV, b'\x07')
    i2c.writeto_mem(address, CONFIG, b'\x00')
    i2c.writeto_mem(address, GYRO_CONFIG, b'\x00')
    i2c.writeto_mem(address, ACCEL_CONFIG, b'\x00')


def read_raw_data(i2c, addr, address=0x68):
    high = i2c.readfrom_mem(address, addr, 1)[0]
    low = i2c.readfrom_mem(address, addr + 1, 1)[0]
    value = high << 8 | low
    if value > 32768:
        value = value - 65536
    return value


def get_mpu6050_data(i2c):
    temp = read_raw_data(i2c, TEMP_OUT_H) / 340.0 + 36.53
    accel_x = read_raw_data(i2c, ACCEL_XOUT_H) / 16384.0
    accel_y = read_raw_data(i2c, ACCEL_XOUT_H + 2) / 16384.0
    accel_z = read_raw_data(i2c, ACCEL_XOUT_H + 4) / 16384.0
    gyro_x = read_raw_data(i2c, GYRO_XOUT_H) / 131.0
    gyro_y = read_raw_data(i2c, GYRO_XOUT_H + 2) / 131.0
    gyro_z = read_raw_data(i2c, GYRO_XOUT_H + 4) / 131.0

    return {
        'temp': temp,
        'accel': {
            'x': accel_x,
            'y': accel_y,
            'z': accel_z,
        },
        'gyro': {
            'x': gyro_x,
            'y': gyro_y,
            'z': gyro_z,
        }
    }


def calculate_tilt_angles(accel_data):
    x, y, z = accel_data['x'], accel_data['y'], accel_data['z']

    tilt_x = math.atan2(y, math.sqrt(x * x + z * z)) * 180 / math.pi
    tilt_y = math.atan2(-x, math.sqrt(y * y + z * z)) * 180 / math.pi
    tilt_z = math.atan2(z, math.sqrt(x * x + y * y)) * 180 / math.pi

    return tilt_x, tilt_y, tilt_z


def complementary_filter(pitch, roll, gyro_data, dt, alpha=0.98):
    pitch += gyro_data['x'] * dt
    roll -= gyro_data['y'] * dt

    pitch = alpha * pitch + (1 - alpha) * math.atan2(gyro_data['y'], math.sqrt(
        gyro_data['x'] * gyro_data['x'] + gyro_data['z'] * gyro_data['z'])) * 180 / math.pi
    roll = alpha * roll + (1 - alpha) * math.atan2(-gyro_data['x'], math.sqrt(
        gyro_data['y'] * gyro_data['y'] + gyro_data['z'] * gyro_data['z'])) * 180 / math.pi

    return pitch, roll


# Specify the SDA and SCL pins
sda_pin = Pin(18)  # replace with your actual pin number
scl_pin = Pin(19)  # replace with your actual pin number

# Create an I2C object with specified pins
i2c = I2C(1, scl=scl_pin, sda=sda_pin, freq=400000)

# Initialize MPU6050
init_mpu6050(i2c)

pitch = 0
roll = 0
prev_time = utime.ticks_ms()

try:
    while True:
        data = get_mpu6050_data(i2c)
        curr_time = utime.ticks_ms()
        dt = (curr_time - prev_time) / 1000

        tilt_x, tilt_y, tilt_z = calculate_tilt_angles(data['accel'])
        pitch, roll = complementary_filter(pitch, roll, data['gyro'], dt)

        prev_time = curr_time

        print("Temperature: {:.2f} °C".format(data['temp']))
        print("Tilt angles: X: {:.2f}, Y: {:.2f}, Z: {:.2f} degrees".format(tilt_x, tilt_y, tilt_z))
        print("Pitch: {:.2f}, Roll: {:.2f} degrees".format(pitch, roll))
        print("Acceleration: X: {:.2f}, Y: {:.2f}, Z: {:.2f} g".format(data['accel']['x'], data['accel']['y'],
                                                                       data['accel']['z']))
        print("Gyroscope: X: {:.2f}, Y: {:.2f}, Z: {:.2f} °/s".format(data['gyro']['x'], data['gyro']['y'],
                                                                      data['gyro']['z']))

        utime.sleep(1)

except KeyboardInterrupt:
    print("Program terminated by user")
