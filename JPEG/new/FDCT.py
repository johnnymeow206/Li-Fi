import numpy as np
from sympy import cos, pi

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