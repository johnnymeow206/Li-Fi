import numpy as np
from sympy import cos, pi
import cv2
import Def
def zigzag(img):
    x = y = z = 0
    X = np.array([0,0,1,2,1,0,0,1,2,3,4,3,2,1,0,0,
                1,2,3,4,5,6,5,4,3,2,1,0,0,1,2,3,
                4,5,6,7,7,6,5,4,3,2,1,2,3,4,5,6,
                7,7,6,5,4,3,4,5,6,7,7,6,5,6,7,7])
    Y = np.array([0,1,0,0,1,2,3,2,1,0,0,1,2,3,4,5,
                4,3,2,1,0,0,1,2,3,4,5,6,7,6,5,4,
                3,2,1,0,1,2,3,4,5,6,7,7,6,5,4,3,
                2,3,4,5,6,7,7,6,5,4,5,6,7,7,6,7])
    Z = np.zeros((64))
    for i in range(64): 
            Z[z] = img[X[i],Y[i]]
            z += 1
    return Z
def izigzag(Z):
    x = y = z = 0
    X = np.array([0,0,1,2,1,0,0,1,2,3,4,3,2,1,0,0,
                1,2,3,4,5,6,5,4,3,2,1,0,0,1,2,3,
                4,5,6,7,7,6,5,4,3,2,1,2,3,4,5,6,
                7,7,6,5,4,3,4,5,6,7,7,6,5,6,7,7])
    Y = np.array([0,1,0,0,1,2,3,2,1,0,0,1,2,3,4,5,
                4,3,2,1,0,0,1,2,3,4,5,6,7,6,5,4,
                3,2,1,0,1,2,3,4,5,6,7,7,6,5,4,3,
                2,3,4,5,6,7,7,6,5,4,5,6,7,7,6,7])
    img = np.zeros((8,8))
    for i in range(64): 
            img[X[i],Y[i]] = Z[z]
            z += 1
    return img

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
iZig_img = izigzag(Zig_img)
#print(iZig_img)
def RLE(Z):
    temp = np.zeros([8,2], dtype=int)
    '''
    for a in range(64):
        temp[1,a] = 
    #return  
    '''
temp = np.zeros([64,2])
a = b = c = 0
while a < 64:
    if Zig_img[a]!=0:
        temp[b] = [0,Zig_img[a]]
        if Zig_img[a-1]==0:
            temp[b] = [c,Zig_img[a]]
        b+=1
    elif Zig_img[a]==0:
        c+=1
    a+=1
RLE = np.resize(temp,(b,2))
print(temp)
