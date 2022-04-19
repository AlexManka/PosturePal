# Add your Python code here. E.g.
from microbit import *
import math
#import csv


while True:

    # Get accelerometer data
    acc = [accelerometer.get_x(), accelerometer.get_y(), accelerometer.get_z()]
    #print("acc_x acc_y acc_z: " + str(acc[0]) + ", " + str(acc[1]) + ", " + str(acc[2]))
    
    """
    # Convert to angles
    theta_denom = math.sqrt(math.pow(acc[1],2) + math.pow(acc[2], 2)) if math.sqrt(math.pow(acc[1],2) + math.pow(acc[2], 2)) else 0.000001
    theta = math.atan(acc[0] / theta_denom) * (180/math.pi)
    
    psi_denom = math.sqrt(math.pow(acc[0],2) + math.pow(acc[2], 2)) if math.sqrt(math.pow(acc[0],2) + math.pow(acc[2], 2)) else 0.000001
    psi = math.atan(acc[1] / psi_denom) * (180/math.pi)
    
    phi_denom = acc[2] if acc[2] else 0.000001
    phi = math.atan(math.sqrt(math.pow(acc[0],2) + math.pow(acc[1], 2)) / phi_denom) * (180/math.pi)
    """
    theta = math.atan2(acc[0], math.sqrt(math.pow(acc[1],2) + math.pow(acc[2], 2))) * (180/math.pi)
    psi = math.atan2(acc[1], math.sqrt(math.pow(acc[0],2) + math.pow(acc[2], 2))) * (180/math.pi)
    phi = math.atan2(math.sqrt(math.pow(acc[0],2) + math.pow(acc[1], 2)), acc[2]) * (180/math.pi)
    
    #print("theta psi phi: " + str(theta) + ", " + str(psi) + ", " + str(phi))
    
    #with open('acc_data.txt', 'w') as f:
    #    f.write('{},{},{},{},{},{}\n'.format(acc[0], acc[1], acc[2], theta, psi, phi))
    
    print(str(acc[0]) + ", " + str(acc[1]) + ", " + str(acc[2]) + ", " + str(theta) + ", " + str(psi) + ", " + str(phi))
    sleep(1000)