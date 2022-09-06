from time import sleep
import serial                         # add Serial library for Serial communication
import numpy as np
from sympy import pi
import cv2
import Def2
import encode
import time
start = time.time()
rows=256
cols=256
channels =1
i = 0
w = 32

img=np.fromfile(r'lena', dtype='uint8')
img=img.reshape(rows, cols, channels)
send_array = encode.encode(img, w)
lf = '00000000000000000000'
SENDING = send_array + lf
############arduino_setup#######################
COM_PORT = 'COM6'
BAUD_RATES = 115200
ser = serial.Serial(COM_PORT, BAUD_RATES, timeout=1) #Create Serial port object called arduinoSerialData
print (ser.readline())          #read the serial data and print it as line
print ("Press enter to send file")
a = len(SENDING)
print(a)
#############MAIN#####################################
#start = input()                                    #infinite loop
while input():                           
    print ("Start Sending")          #prints the data for confirmation
    for i in range(a):
        
        if (SENDING[i] == '1'):                   #if the entered data is 1 
            ser.write(b'1')             #send 1 to arduino
            print ("LED ON")
        
        else:                                   #if the entered data is 0
            ser.write(b'0')             #send 0 to arduino 
            print ("LED OFF")
        
        sleep(0.005)


