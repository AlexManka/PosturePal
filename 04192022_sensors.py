from microbit import *
import math

n = 2 # number of bytes read from SCL and SDA pins

while True:

    i2c.init()
    devices = i2c.scan() # Returns list of addresses corresponding to devices that responded to scan
    print(devices)
    
    # Uncomment these lines once scan() returns something (i.e. devices is not an empty list)
    #imu1_reading = 2c.read(devices[0], n, repeat=False)
    #imu2_reading = i2c.read(devices[1], n, repeat=False)
    #print(imu1_reading, imu2_reading)