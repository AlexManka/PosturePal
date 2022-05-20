# Add your Python code here. E.g.
from microbit import *
import math
import ustruct


i2c.init(freq=100000, sda=pin20, scl=pin19)

# Scan the i2caddrs
# print(int(i2c.scan()[0]))
i2caddrs = [104, 105]

# Takes in a reg (int) and data (hex/bin)
def write_reg(i2caddr, reg_addr, data):
    i2c.write(i2caddr, reg_addr.to_bytes(1, 'big') + data)

# Takes in a reg (int) and number of bytes to read n (int)
def read_reg(i2caddr, reg_addr, n):
    i2c.write(i2caddr, reg_addr.to_bytes(1, 'big'))
    return i2c.read(i2caddr, n)
    
# Uses accelerometer readings to calculate x, y, and z axis angles    
def calculate_acc_angles(x_acc, y_acc, z_acc):
    theta = math.atan2(x_acc, math.sqrt(math.pow(y_acc,2) + math.pow(z_acc, 2))) * (180/math.pi)
    psi = math.atan2(y_acc, math.sqrt(math.pow(x_acc,2) + math.pow(z_acc, 2))) * (180/math.pi)
    phi = math.atan2(math.sqrt(math.pow(x_acc,2) + math.pow(y_acc, 2)), z_acc) * (180/math.pi)
    return theta, psi, phi
    
# Fuses accelerometer and gyroscope readings to calculate final z axis angle    
def calculate_z_axis_angle(old_tilt_angle, dt, phi, gyro_reading):
    alpha = 0.98
    tilt_angle = old_tilt_angle - 1 + gyro_reading * dt
    z_angle = alpha * tilt_angle + (1 - alpha) * phi
    return z_angle, tilt_angle

# Acceleration and gyroscope conversion factors (from datasheet)
aconv = 16384.0
gconv = 131.0



while True:
    for i2caddr in i2caddrs:
        
        print("i2caddr: " + str(i2caddr))
        
        #AccX
        axhi = read_reg(i2caddr, 59, 1)
        axlo = read_reg(i2caddr, 60, 1)
        ax = axhi + axlo
        
        #AccY
        ayhi = read_reg(i2caddr, 61, 1)
        aylo = read_reg(i2caddr, 62, 1)
        ay = ayhi + aylo
        
        #AccZ
        azhi = read_reg(i2caddr, 63, 1)
        azlo = read_reg(i2caddr, 64, 1)
        az = azhi + azlo
        
        acc_x = ustruct.unpack(">h", ax)[0] / aconv
        print("signed_acc_x: " + str(acc_x))
        acc_y = ustruct.unpack(">h", ay)[0] / aconv
        print("signed_acc_y: " + str(acc_y))
        acc_z = ustruct.unpack(">h", az)[0] / aconv
        print("signed_acc_z: " + str(acc_z))
        print('\n')
        
        # Calculate angles
        theta, psi, phi = calculate_acc_angles(acc_x, acc_y, acc_z)
        print("theta: " + str(theta))
        print("psi: " + str(psi))
        print("phi: " + str(phi))
        
        
        # Gyroscope code
        i2c.write(104, b'\x45', repeat = False)
        gyro_reading0 = i2c.read(i2caddr, 1)
        i2c.write(104, b'\x46', repeat = False)
        gyro_reading1 = i2c.read(i2caddr,1)
        gyro_reading = (gyro_reading0 + gyro_reading1)
        gyro_sint = ustruct.unpack(">h", gyro_reading)[0] / gconv
        print("gyro reading: " + str(gyro_sint))
        
        
        # Set 0 to high, then low (for vibromotor)
        pin0.write_digital(1)
        sleep(1000)
        pin0.write_digital(0)
        sleep(1000)
        print("\n")
