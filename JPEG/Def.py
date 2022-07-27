import numpy as np
from sympy import cos

def FDCT_for_gray(img):
    img2 = img
    img_DCT = img
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

def RLE_AC(array1):
    array2 = array1
    array3 = [int(array2[0])]
    k = 0

    for i in range (63):   
        if array2[i+1] == 0:
            k += 1
            if  i+1 == 63:
                array3.append("EOB")
                break
        else:
            array3.append([k,int(array2[i+1])])
            k = 0
    return array3

def InvRLE_AC(array1):
    array2 = array1
    array3 = [array2[0]]
    i = 1

    while array2[i][0] != 'E':
            array3.extend([0]*int(array2[i][0]))
            array3.append(array2[i][1])
            i += 1
    
    array3.extend([0]*(64 - len(array3)))
    return array3