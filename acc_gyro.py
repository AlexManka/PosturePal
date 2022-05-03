# Add your Python code here. E.g.
from microbit import *
import math

i2c.init(freq=100000, sda=pin20, scl=pin19)
# print(int(i2c.scan()[0]))
# 104 was printed
i2caddr = 104

# takes in a reg (int) and data (hex/bin)
def write_reg(reg_addr, data):
    i2c.write(i2caddr, reg_addr.to_bytes(1, 'big') + data)

# takes in a reg (int) and number of bytes to read n (int)
def read_reg(reg_addr, n):
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

# acceleration conversion factor (from datasheet)
aconv = 16384.0


# write_reg(119, b'\x00')
# write_reg(120, b'\x00')
# write_reg(122, b'\x00')
# write_reg(123, b'\x00')
# write_reg(125, b'\x00')
# write_reg(126, b'\x00')



while True:
    #AccX
    axhi = read_reg(59, 1)
    axlo = read_reg(60, 1)
    ax = axhi + axlo
    
    #AccY
    ayhi = read_reg(61, 1)
    aylo = read_reg(62, 1)
    ay = ayhi + aylo
    
    #AccZ
    azhi = read_reg(63, 1)
    azlo = read_reg(64, 1)
    az = azhi + azlo
    
    acc_x = int.from_bytes(ax, 'big') / aconv
    print(acc_x)
    print(" ")
    acc_y = int.from_bytes(ay, 'big') / aconv
    print(acc_y)
    print(" ")
    acc_z = int.from_bytes(az, 'big') / aconv
    print(acc_z)
    print('\n')
    
    
    # WHO AM I 
    #print(int.from_bytes(read_reg(117, 1), 'big'))
    
    
    # Print out the micro:bit values
    microbit_scale_factor = 3.9 / 1000
    microbit_acc = accelerometer.get_values()
    microbit_x_acc = microbit_acc[0] * microbit_scale_factor
    microbit_y_acc = microbit_acc[1] * microbit_scale_factor
    microbit_z_acc = microbit_acc[2] * microbit_scale_factor
    print(microbit_x_acc, microbit_y_acc, microbit_z_acc)
    print('\n\n')
    
    theta, psi, phi = calculate_acc_angles(microbit_x_acc, microbit_y_acc, microbit_z_acc)
    print("theta: " + str(theta))
    print("psi: " + str(psi))
    print("phi: " + str(phi))
    
    # print(read_reg(119, 1))
    # print(read_reg(120, 1))
    # print(read_reg(122, 1))
    # print(read_reg(123, 1))
    # print(read_reg(125, 1))
    # print(read_reg(126, 1))

    sleep(100)




