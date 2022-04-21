from microbit import *
import math

n = 64 # number of bytes read from SCL and SDA pins
i2c.init()
devices = i2c.scan() # Returns list of addresses corresponding to devices that responded to scan
print(devices)

while True:
    imu1_reading = i2c.read(devices[0], n, repeat=False)
    #imu2_reading = i2c.read(devices[1], n, repeat=False)
    imu1_accel = imu1_reading[59:64]
    #output = int.from_bytes(imu1_accel, "little")
    print(imu1_accel)
    sleep(1000)