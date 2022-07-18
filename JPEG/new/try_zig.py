import numpy as np
from sympy import cos, pi
import cv2
import Def
def zigzag(img):
    Z = np.zeros((64))
    z, c, d = 0, 0, 0
    while z < 64:
        while c == 0 or d == 7:
            if c == 0 and d == 0:
                Z[z] = img[c,d]
                print(Z[z])
            d += 1
            Z[z] = img[c,d]
            print(Z[z])
            z+=1
            c+=1
            d-=1
            Z[z] = img[c,d]
            print(Z[z])
            z+=1
            if d != 0:
                c+=1
                d-=1
                Z[z] = img[c,d]
                print(Z[z])
                z+=1
        while d == 0 or c == 7:
            c+=1
            Z[z] = img[c,d]
            print(Z[z])
            z+=1
            c-=1
            d+=1
            Z[z] = img[c,d]
            print(Z[z])
            z+=1
            if c != 0:
                c-=1
                d+=1
                Z[z] = img[c,d]
                print(Z[z])
                z+=1
    return Z
zig = np.array([[0,1,5,6,14,15,27,28],
                [2,4,7,13,16,26,29,42],
                [3,8,12,17,25,30,41,43],
                [9,11,18,24,31,40,44,53],
                [10,19,23,32,39,45,52,54],
                [20,22,33,38,46,51,55,60],
                [21,34,37,47,50,56,59,61],
                [35,36,48,49,57,58,62,63]])
zig = np.asmatrix(zig)
Zig_img = zigzag(zig)
print(Zig_img)