from PIL import Image
import numpy as np
from sympy import cos, pi
import FDCT
import cv2
import Def

rows=256
cols=256
channels =1
i = 0

img=np.fromfile(r'lena', dtype='uint8')
img=img.reshape(rows, cols, channels)

img = np.transpose(img) 
img1 = np.split(img, 32, axis=1)

#print(np.array(img1[0]))

img1[0] = np.transpose(img1[0])

img2 = np.split(img1[0], 32)
img2[0] = np.transpose(img2[0])
print(img2[0])
img2y = np.asmatrix(img2[0])
'''
def FDCT_for_gray(img):
    N = 8
    img2 = img
    img2 = np.asmatrix(img2)
    img2 = img2 - np.ones((8,8))*128
    sum = 0
    for u in range(8):
        for  v in range(8):   
            for x in range(8):
                for  y in range(8):    
                    if u == 0 and v == 0:
                        cucv = 1/1.414
                    else:
                        cucv = 1
                    sum += (2*cucv/N)*(img2[x,y]*cos(((2*x+1)*u*pi.evalf())/(2*N))*cos(((2*y+1)*v*pi.evalf())/(2*N)))
            img2[u,v] =sum
            sum = 0
    return img2
print(FDCT_for_gray(img2[0]))
'''
img2y = img2y - np.ones((8,8))*128
dct_img = cv2.dct(img2y)
print(dct_img)
'''
idct_img = cv2.idct(dct_img)
print(idct_img)
'''
Quan_img = Def.quan(dct_img)
for x in range(8):
    for y in range(8):
        Quan_img[x,y] = round(Quan_img[x,y])
print(Quan_img)

