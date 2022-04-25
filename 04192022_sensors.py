# Add your Python code here. E.g.
from microbit import *

display.scroll("Posture Pal", wait=False, loop=True)

# INIT I2C
i2c.init(freq=100000, sda=pin20, scl=pin19)
devices = i2c.scan()
print(devices)

# CHECK WAI ON MPU0
i2c.write(104, b'\x75')
wai_reading = i2c.read(104, 1, repeat=False)
WAI0 = int.from_bytes(wai_reading, "little")
print(WAI0) # should return 0x71 or 113


while True:
    i2c.write(104, b'\x3b', repeat=False)
    ACCEL0_X_H = i2c.read(104, 1, repeat=False)
    sleep(1)
    i2c.write(104, b'\x3c', repeat=False)
    ACCEL0_X_L = i2c.read(104, 1, repeat=False)
    ACCEL0_X = ACCEL0_X_H + ACCEL0_X_L
    print(ACCEL0_X)
    
    #i2c.write(104, b'\x3d')
    #ACCEL0_Y_H = i2c.read(104, 1, repeat=False)
    #sleep(1)
    #i2c.write(104, b'\x3e')
    #ACCEL0_Y_L = i2c.read(104, 1, repeat=False)
    #ACCEL0_Y = ACCEL0_Y_H + ACCEL0_Y_L
    #print(ACCEL0_Y)
    
    #i2c.write(104, b'\x47')
    #ACCEL0_Z_H = i2c.read(104, 1, repeat=False)
    #i2c.write(104, b'\x48')
    #ACCEL0_Z_L = i2c.read(104, 1, repeat=False)
    #ACCEL0_Z = ACCEL0_Z_H + ACCEL0_Z_L
    #print(ACCEL0_Z)
    
    i2c.write(104, b'\x43', repeat=False)
    GYRO0_X_H = i2c.read(104, 1, repeat=False)
    sleep(1)
    i2c.write(104, b'\x44', repeat=False)
    GYRO0_X_L = i2c.read(104, 1, repeat=False)
    GYRO0_X = GYRO0_X_H + GYRO0_X_L
    print(GYRO0_X)
    
    print('\n')

    sleep(1000)
