import serial
import numpy as np
import combine_main

rows=256
cols=256
channels =1
w = 32
i = 0
t = 16

img=np.fromfile(r'lena', dtype='uint8')
img=img.reshape(rows, cols, channels)
abc = combine_main.encode(img)
if __name__ == '__main__':
  com = serial.Serial('COM3',115200)
  success_bytes = com.write(str.encode(abc))
  print(success_bytes)