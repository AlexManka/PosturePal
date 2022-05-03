# Add your Python code here. E.g.
from microbit import *
import struct

display.scroll("Posture Pal", wait=False, loop=True)

# INIT I2C
i2c.init(freq=400000, sda=pin20, scl=pin19)
devices = i2c.scan()
print(devices)

i2c.write(104, b'\x1C')
i2c.write(104, b'00000000', repeat=False)

# CHECK WAI ON MPU0
i2c.write(104, struct.pack('B', 117))
#i2c.write(104, b'\x75', repeat = True)
wai_reading = i2c.read(104, 1, repeat=False)
WAI0 = int.from_bytes(wai_reading, "big")
print(WAI0) # should return 0x71 or 113


while True:
    i2c.write(104, b'\x45', repeat = False)
    gyro_reading0 = i2c.read(104, 1)
    i2c.write(104, b'\x46', repeat = False)
    gyro_reading1 = i2c.read(104,1)
    gyro_reading = (gyro_reading0 + gyro_reading1)
    gyro_int = int.from_bytes(gyro_reading, byteorder='big', signed=True)/131
    print(gyro_int)
    #buf = b'\x3B'
    #i2c.write(104, buf, repeat=False)
    #ACCEL0_X_H = i2c.read(104, 1, repeat=False)
    #buf = b'\x3C'
    #i2c.write(104, buf, repeat=False)
    #ACCEL0_X_L = i2c.read(104, 1, repeat=False)
    #ACCEL0_X = ACCEL0_X_H + ACCEL0_X_L
    #test = int.from_bytes(ACCEL0_X, "big")
    #print(test)
    
    #i2c.write(104, b'\x0d', repeat=False)
    #test = i2c.read(104, 1, repeat=False)
    #print(test)
    
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
    
    #i2c.write(104, b'\x43', repeat=True)
    #GYRO0_X_H = i2c.read(104, 1, repeat=False)
    #sleep(10)
    #i2c.write(104, b'\x44', repeat=True)
    #GYRO0_X_L = i2c.read(104, 1, repeat=False)
    #GYRO0_X = GYRO0_X_H + GYRO0_X_L
    #gyro = int.from_bytes(GYRO0_X, "big")   
    #print(gyro)
    
    print(accelerometer.get_values())
    
    print('\n')

    sleep(600)
