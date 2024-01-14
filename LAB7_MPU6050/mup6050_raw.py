import machine
import utime

# I2C address of the MPU-6050
MPU6050_I2C_ADDR = 0x68

# Create I2C object
i2c = machine.I2C(1, scl=machine.Pin(19), sda=machine.Pin(18), freq=400000)

def read_accel_gyro():
    # Read accelerometer and gyroscope data from MPU-6050
    accel_data = i2c.readfrom_mem(MPU6050_I2C_ADDR, 0x3B, 14)
    accel_x = (accel_data[0] << 8) | accel_data[1]
    accel_y = (accel_data[2] << 8) | accel_data[3]
    accel_z = (accel_data[4] << 8) | accel_data[5]

    gyro_x = (accel_data[8] << 8) | accel_data[9]
    gyro_y = (accel_data[10] << 8) | accel_data[11]
    gyro_z = (accel_data[12] << 8) | accel_data[13]

    return accel_x, accel_y, accel_z, gyro_x, gyro_y, gyro_z

try:
    while True:
        accel_x, accel_y, accel_z, gyro_x, gyro_y, gyro_z = read_accel_gyro()
        print("Accelerometer (X,Y,Z):", accel_x, accel_y, accel_z)
        print("Gyroscope (X,Y,Z):", gyro_x, gyro_y, gyro_z)
        utime.sleep(1)

except KeyboardInterrupt:
    print("Program terminated by user")
