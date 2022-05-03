# Add your Python code here. E.g.
from microbit import *

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
    print(int.from_bytes(ax, 'big') / aconv)
    print(" ")
    print(int.from_bytes(ay, 'big') / aconv)
    print(" ")
    print(int.from_bytes(az, 'big') / aconv)
    print('\n')
    
    # WHO AM I 
    #print(int.from_bytes(read_reg(117, 1), 'big'))
    
    
    # Print out the micro:bit values
    print(accelerometer.get_values())
    print('\n\n')
    
    # print(read_reg(119, 1))
    # print(read_reg(120, 1))
    # print(read_reg(122, 1))
    # print(read_reg(123, 1))
    # print(read_reg(125, 1))
    # print(read_reg(126, 1))

    sleep(100)
