import machine
import time
import math

# Set up the I2C interface using the primary I2C pins (SCL=9, SDA=8)
i2c = machine.I2C(1, sda=machine.Pin(18), scl=machine.Pin(19))

# MPU-6050 I2C address
MPU6050_I2C_ADDR = 0x68

# Wake up the MPU-6050 from sleep
i2c.writeto_mem(MPU6050_I2C_ADDR, 0x6B, b'\x00')

def read_accel_gyro():
    # Read accelerometer data
    accel_x = i2c.readfrom_mem(MPU6050_I2C_ADDR, 0x3B, 2)
    accel_y = i2c.readfrom_mem(MPU6050_I2C_ADDR, 0x3D, 2)
    accel_z = i2c.readfrom_mem(MPU6050_I2C_ADDR, 0x3F, 2)

    # Combine the high and low bytes
    accel_x = (accel_x[0] << 8) | accel_x[1]
    accel_y = (accel_y[0] << 8) | accel_y[1]
    accel_z = (accel_z[0] << 8) | accel_z[1]

    # Read gyroscope data
    gyro_x = i2c.readfrom_mem(MPU6050_I2C_ADDR, 0x43, 2)
    gyro_y = i2c.readfrom_mem(MPU6050_I2C_ADDR, 0x45, 2)
    gyro_z = i2c.readfrom_mem(MPU6050_I2C_ADDR, 0x47, 2)

    # Combine the high and low bytes
    gyro_x = (gyro_x[0] << 8) | gyro_x[1]
    gyro_y = (gyro_y[0] << 8) | gyro_y[1]
    gyro_z = (gyro_z[0] << 8) | gyro_z[1]

    return accel_x, accel_y, accel_z, gyro_x, gyro_y, gyro_z

def convert_to_degrees(raw_value):
    # Conversion to degrees
    sensitivity = 16384.0  # Sensitivity for +/- 2g range (accelerometer)
    g_force = raw_value / sensitivity
    angle_in_degrees = math.degrees(math.asin(max(-1, min(1, g_force))))
    return angle_in_degrees

while True:
    accel_x, accel_y, accel_z, gyro_x, gyro_y, gyro_z = read_accel_gyro()

    # Convert accelerometer readings to degrees
    accel_angle_x = convert_to_degrees(accel_x)
    accel_angle_y = convert_to_degrees(accel_y)
    accel_angle_z = convert_to_degrees(accel_z)

    # Convert gyroscope readings to degrees per second
    gyro_rate_x = gyro_x / 131.0  # Sensitivity for +/- 250 degrees/s range (gyroscope)
    gyro_rate_y = gyro_y / 131.0
    gyro_rate_z = gyro_z / 131.0

    print("Accelerometer Angles (X, Y, Z): {:.2f}°, {:.2f}°, {:.2f}°".format(accel_angle_x, accel_angle_y, accel_angle_z))
    print("Gyroscope Rates (X, Y, Z): {:.2f}°/s, {:.2f}°/s, {:.2f}°/s".format(gyro_rate_x, gyro_rate_y, gyro_rate_z))

    time.sleep(0.1)  # Adjust sleep duration as needed
