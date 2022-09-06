import numpy as np
import math
from math import cos, pi

def FDCT3(S):
    F = np.ones((8,8))
    M = []
    m0 = np.array([1/(2*math.sqrt(2)) for x in range (8)])
    m1 = [[0 for k1 in range(8)] for k2 in range(7)]
    for u0 in range(7):
        u = u0+1
        m1[u0] = np.array([0.5*math.cos(((2*v+1)*u*math.pi)/16) for v in range (8)])
    M = np.asmatrix(np.vstack((m0,m1)))
    F = M*S*np.transpose(M)
    return F

def quan(img): #要改用陣列表示省掉一個迴圈
    quan =np.array([[16,11,10,16,24,40,51,61],
                    [12,12,14,19,26,58,60,55],
                    [14,13,16,24,40,57,69,56],
                    [14,17,22,29,51,87,80,62],
                    [18,22,37,56,68,109,103,77],
                    [24,35,55,64,81,104,113,92],
                    [49,64,78,87,103,121,120,101],
                    [72,92,95,98,112,100,103,99]])
    quan = np.asmatrix(quan)
    for x in range(8):
        for y in range(8):
            img[x,y] = img[x,y]/quan[x,y]
    return img
'''
def quan_try(img,Q): #要改用陣列表示省掉一個迴圈
    if Q<1:
        Q=1
    elif Q>99:
        Q=99
    if Q<50:
        S = 5000/Q
    else:
        S = 200 - 2*Q
    new_quan = np.ones((8,8))
    base_quan=np.array([[16,11,10,16,24,40,51,61],
                        [12,12,14,19,26,58,60,55],
                        [14,13,16,24,40,57,69,56],
                        [14,17,22,29,51,87,80,62],
                        [18,22,37,56,68,109,103,77],
                        [24,35,55,64,81,104,113,92],
                        [49,64,78,87,103,121,120,101],
                        [72,92,95,98,112,100,103,99]])
    quan = np.asmatrix(base_quan)
    for x in range(8):
        for y in range(8):
            new_quan[x,y]=(quan[x,y]*S+50)/100
            if new_quan[x,y]<1:
                new_quan[x,y]=1
            img[x,y] = img[x,y]/new_quan[x,y]
    return img
'''
def zigzag(img):
    z = 0
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
            if k > 15:
                k = 15
                array3.append([k,0])
                k = 0
            array3.append([k,int(array2[i+1])])
            k = 0
    return array3

def InvRLE_AC(array1): #haven't check  now
    array2 = array1
    array3 = [array2[0]]
    i = 1

    while array2[i][0] != 'E':
        if array2[i] == [15,0]:
            array3.extend([0]*16)
            i+=1
        else:
            array3.extend([0]*int(array2[i][0]))
            array3.append(array2[i][1])
            i += 1
    
    array3.extend([0]*(64 - len(array3)))
    return array3

def izigzag(Z):
    z = 0
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

def iquan(img):
    iquan =np.array([[16,11,10,16,24,40,51,61],
                     [12,12,14,19,26,58,60,55],
                     [14,13,16,24,40,57,69,56],
                     [14,17,22,29,51,87,80,62],
                     [18,22,37,56,68,109,103,77],
                     [24,35,55,64,81,104,113,92],
                     [49,64,78,87,103,121,120,101],
                     [72,92,95,98,112,100,103,99]])
    iquan = np.asmatrix(iquan)
    for x in range(8):
        for y in range(8):
            img[x,y] = img[x,y]*iquan[x,y]
    return img
'''
def iquan_try(img,Q): #要改用陣列表示省掉一個迴圈
    if Q<1:
        Q=1
    elif Q>99:
        Q=99
    if Q<50:
        S = 5000/Q
    else:
        S = 200 - 2*Q
    new_iquan = np.ones((8,8))
    base_iquan=np.array([[16,11,10,16,24,40,51,61],
                        [12,12,14,19,26,58,60,55],
                        [14,13,16,24,40,57,69,56],
                        [14,17,22,29,51,87,80,62],
                        [18,22,37,56,68,109,103,77],
                        [24,35,55,64,81,104,113,92],
                        [49,64,78,87,103,121,120,101],
                        [72,92,95,98,112,100,103,99]])
    iquan = np.asmatrix(base_iquan)
    for x in range(8):
        for y in range(8):
            new_iquan[x,y]=(iquan[x,y]*S+50)/100
            if new_iquan[x,y]<1:
                new_iquan[x,y]=1
            img[x,y] = img[x,y]*new_iquan[x,y]
    return img
'''
def iFDCT3(S1):
    f = np.ones((8,8))
    M = []
    m0 = np.array([1/(2*math.sqrt(2)) for x in range (8)])
    m1 = [[0 for k1 in range(8)] for k2 in range(7)]
    for u0 in range(7):
        u = u0+1
        m1[u0] = np.array([0.5*math.cos(((2*v+1)*u*math.pi)/16) for v in range (8)])
    M = np.asmatrix(np.vstack((m0,m1)))
    f = np.transpose(M)*S1*M
    return f


