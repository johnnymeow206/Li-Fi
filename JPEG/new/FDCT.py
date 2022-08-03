import numpy as np
from sympy import cos, pi
import cv2
import time

#start = time.time()

def FDCT_for_gray(img):
    img2 = img
    img_DCT = img
    img2 = np.asmatrix(img2)
    img2 = img2 - np.ones((8,8))*128
    sum = 0
    pi = 3.14159
    for u in range(8):
        for  v in range(8):   
            for x in range(8):
                for y in range(8):    
                    if u == 0 and v == 0:
                        cucv = 1/2
                    else:
                        cucv = 1
                    sum += (cucv/4)*(img2[x,y]*cos(((2*x+1)*u*pi)/16)*cos(((2*y+1)*v*pi)/16))
            img_DCT[u,v] = sum
            sum = 0
    img_DCT =img_DCT.astype(np.float32)
    return img_DCT
def iFDCT_for_gray(img_iDCT0):
    img_iDCT1 = img_iDCT0
    img_iDCT1 = np.asmatrix(img_iDCT1)
    img_iDCT = np.zeros((8,8))
    img_iDCT = np.asmatrix(img_iDCT)
    sum = 0
    pi = 3.14159
    for x in range(8):
        for  y in range(8):   
            for u in range(8):
                for v in range(8):    
                    if u == 0 and v == 0:
                        cucv = 1/2
                    else:
                        cucv = 1
                    sum += (cucv)*(img_iDCT1[u,v]*cos(((2*x+1)*u*pi)/16)*cos(((2*y+1)*v*pi)/16))     
            img_iDCT[x,y] = sum/4
            sum = 0
    img_iDCT = img_iDCT + np.ones((8,8))*128
    img_iDCT =img_iDCT.astype(np.float32)
    return img_iDCT
'''
def iFDCT_for_gray(img):
    img3 = img
    img4 = np.zeros((8,8))
    img4 = np.asmatrix(img4)
    img3 = np.asmatrix(img3)
    sum = 0
    pi = 3.14159
    for x in range(8):
        for  y in range(8):   
            for u in range(8):
                for v in range(8):    
                    if u == 0 and v == 0:
                        cucv = 1/2
                    else:
                        cucv = 1
                    sum += (cucv/4)*(img3[u,v]*cos(((2*x+1)*u*pi)/16)*cos(((2*y+1)*v*pi)/16))
            img4[x,y] = sum
            sum = 0
    img4 = img4 + np.ones((8,8))*128
    return img4

img0 = np.ones((8,8))*255
#print(img0)
img_DCT = FDCT_for_gray(img0)
print(img_DCT)
img_iDCT = iFDCT_for_gray(img_DCT)
print(img_iDCT)

end = time.time()
print(format(end-start))
'''