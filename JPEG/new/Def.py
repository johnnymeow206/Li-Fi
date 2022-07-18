import numpy as np
from sympy import cos, pi
import cv2

def quan(img):
    quan =np.array([[16,11,10,16,24,40,51,61],
                [12,12,14,19,26,58,60,55],
                [14,13,16,24,40,57,69,56],
                [14,17,22,19,51,87,80,62],
                [18,22,37,56,68,109,103,77],
                [24,35,55,64,81,104,113,92],
                [49,64,78,87,103,121,120,101],
                [72,92,95,98,112,100,103,99]])
    quan = np.asmatrix(quan)
    for x in range(8):
        for y in range(8):
            img[x,y] = img[x,y]/quan[x,y]
    return img
def iquan(img):
    iquan =np.array([[16,11,10,16,24,40,51,61],
                [12,12,14,19,26,58,60,55],
                [14,13,16,24,40,57,69,56],
                [14,17,22,19,51,87,80,62],
                [18,22,37,56,68,109,103,77],
                [24,35,55,64,81,104,113,92],
                [49,64,78,87,103,121,120,101],
                [72,92,95,98,112,100,103,99]])
    iquan = np.asmatrix(iquan)
    for x in range(8):
        for y in range(8):
            img[x,y] = img[x,y]*iquan[x,y]
    return img
def zigzag(img):
    Z = np.zeros((1, 64))
    z, c, d = 0, 0, 0
    while z < 64:
        while c == 0 and d == 0:
            Z[0,z] = img[c,d]
            print(Z[0,z])
        while c == 0 or d == 7:
            d += 1
            Z[0,z] = img[c,d]
            print(Z[0,z])
            z+=1
            c+=1
            d-=1
            Z[0,z] = img[c,d]
            print(Z[0,z])
            z+=1
            if d != 0:
                c+=1
                d-=1
                Z[0,z] = img[c,d]
                print(Z[0,z])
                z+=1
        while d == 0 or c == 7:
            c+=1
            Z[0,z] = img[c,d]
            print(Z[0,z])
            z+=1
            c-=1
            d+=1
            Z[0,z] = img[c,d]
            print(Z[0,z])
            z+=1
            if c != 0:
                c-=1
                d+=1
                Z[0,z] = img[c,d]
                print(Z[0,z])
                z+=1
    return Z
