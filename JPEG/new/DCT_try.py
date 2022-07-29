import numpy as np
from sympy import cos
import cv2

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
    return img_DCT
def FDCT_for_2x2(img):
    img2 = img
    img3 = img
    img2 = np.asmatrix(img2)
    img2 = img2 - np.ones((2,2))*128
    sum = 0
    pi = 3.14159
    for u in range(2):
        for  v in range(2):   
            for x in range(2):
                for y in range(2):    
                    if u == 0 and v == 0:
                        cucv = 1/2
                    else:
                        cucv = 1
                    sum += (cucv)*(img2[x,y]*cos(((2*x+1)*u*pi)/4)*cos(((2*y+1)*v*pi)/4))
                    
            img3[u,v] = sum
            sum = 0
    return img3
def iFDCT_for_2x2(img):
    img3 = img
    img4 = [[0, 0], [0, 0]]
    img4 = np.asmatrix(img4)
    img3 = np.asmatrix(img3)
    sum = 0
    pi = 3.14159
    for x in range(2):
        for  y in range(2):   
            for u in range(2):
                for v in range(2):    
                    if u == 0 and v == 0:
                        cucv = 1/2
                    else:
                        cucv = 1
                    sum += (cucv)*(img3[u,v]*cos(((2*x+1)*u*pi)/4)*cos(((2*y+1)*v*pi)/4))
                    print(img3)
                    print(img4)
                    print(sum)
            img4[x,y] = sum
            sum = 0
    img4 = img4 + np.ones((2,2))*128
    return img4
img = np.array([[255, 255],
                [255, 255]])
img2_DCT = FDCT_for_2x2(img)
print(img2_DCT)
img2_iDCT= iFDCT_for_2x2(img2_DCT)
print(img2_iDCT)
'''
img4 = np.array([[127, 127],
                [127, 127]])
img4 = np.asmatrix(img4)
img4 = np.float32(img4)
img4 = cv2.dct(img4)
print(img4)
img4 = cv2.idct(img4)
print(img4)
'''