from time import sleep
import serial                         # add Serial library for Serial communication
import numpy as np
from sympy import pi
import cv2
import Def2
import time
import decode
start = time.time()
rows=256
cols=256
channels =1
i = 0
w = 32


receive =''
############arduino_setup#######################
COM_PORT = 'COM4'
BAUD_RATES = 115200
ser = serial.Serial(COM_PORT, BAUD_RATES,timeout=1) #Create Serial port object called arduinoSerialData
      


#############RECEIVE#####################################
#start = input()                   #infinite loop                           
expected = '00000000000000000000'
string = ''
print ("Stsrt receiving")          #prints the data for confirmation
receive = ser.read_until(expected, None)
string = receive.decode()
RECEIVE = string[:-20] 
receive_decode = decode.decode(RECEIVE, w)

#######DECODE######################################

img_merge = [[0 for k1 in range(8)] for k2 in range(w)]
for c in range(w):
    img_merge[c] = receive_decode[c][0]
    b = 1
    for a in range(w-1):
        img_merge[c] = np.hstack((img_merge[c],receive_decode[c][b]))
        b+=1

img_merge1 = img_merge[0]
e = 0
f = 1
for d in range(w-1):
    img_merge1 = np.vstack((img_merge1,img_merge[f]))
    e+=1 
    f+=1

img_merge1 = np.transpose(img_merge1)
img_merge1 = img_merge1.astype(np.uint8)
img_merge1=img_merge1.reshape(rows, cols, channels)
cv2.imshow('temp', img_merge1)
cv2.waitKey(0) 

