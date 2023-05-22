# - - coding: utf-8 -*-
"""
 Created on Thu Aug 17 13:25:46 2017
@author: glassbox
"""

"""Module importation"""
import serial
"""Opening of the serial port"""
try:
    arduino = serial.Serial('COM8')
except:
    print( 'Please check the port')

"""Initialising variables
rawdata=[]
count=0

"""
"""Receiving data and storing it in a list"""
""""
while count<3:
    rawdata.append(str(arduino.readline()))
    count+=1
print(rawdata) 
"""
print(arduino)
arduino.close()