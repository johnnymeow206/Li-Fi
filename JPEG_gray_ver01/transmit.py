from time import sleep
import serial 
import math                        # add Serial library for Serial communication
import numpy as np
from sympy import pi
import cv2
import Def2
import encode
import time
import os
import sys
import serial.tools.list_ports
###############################arduino_setup#######################
print("Search...")
ports = serial.tools.list_ports.comports(include_links=False)
for port in ports :
    print("Find port ", port.device)

ser = serial.Serial(port.device)
if ser.isOpen():
    ser.close()

ser = serial.Serial(port.device, 115200)
ser.flushInput()
ser.flushOutput()
print("Connect", ser.name)
def Transmit_Codeword(input_codeword):
    send_array = input_codeword
    lf ='1000000000000000000001S'
    temp = '1'+ send_array + lf

    a = len(temp)
    print("Size to transfer:",a)
    print ("Press enter to send file")
    buffer_size = 64
    n = math.ceil(a/64)
    temp = [temp[idx : idx + buffer_size] for idx in range(0, len(temp), buffer_size)]
    return temp, n


def transmit_to_Board(input_codeword):                                           #infinite loop
    SENDING, n = Transmit_Codeword(input_codeword)
    print ("Start Sending")                  #prints the data for confirmation
    ser.flush()
    for i in range(n):
        ser.write(SENDING[i].encode())                  
        print(SENDING[i])  
    myBytes = ser.read(1).decode() 
    
    # Checks for more bytes in the input buffer
    bufferBytes = ser.inWaiting()
    # If exists, it is added to the myBytes variable with previously read information
    if bufferBytes:
        myBytes = myBytes + ser.read(bufferBytes).decode()
        print(myBytes)
    time.sleep(0.01) 
"""  
while True:                           
#print ("Start Sending")                  #prints the data for confirmation
    sleep(0.01)       
    ser.write(b'1')                     
    print ("LED ON")
    sleep(0.01)        
    ser.write(b'0')                         
    print ("LED OFF")
 """   

    

               


