
import cv2
from PIL import Image
import numpy as np
from sympy import cos
import FDCT
from scipy.fftpack import dct, idct
def rgb_to_y(img_array):
    B,G,R = img_array[0], img_array[1], img_array[2]
    return 0.299 * R + 0.587 * G + 0.114 * B
img = np.zeros((8,8,3), dtype='uint8')   # 快速產生 500x500，每個項目為 [0,0,0] 的三維陣列
img[:8,:8] = [255,255,255]  # 將中間 200x200 的每個項目內容，改為 [255,255,255]
img = np.transpose(img) #讓陣列由列變成行?
imgy = rgb_to_y(img)
print(imgy)
'''
def FDCT_for_gray(img):
    N = 8
    img2 = img
    img2 = np.asmatrix(img2)
    img2 = img2 - np.ones((8,8))*128
    sum = 0
    pi = 3.1415927
    cu = cv = 0
    for u in range(8):
        for  v in range(8):   
            for x in range(8):
                for y in range(8): 
                    if u == 0:
                        cu = 1/1.414
                    elif v == 0:
                        cv = 1/1/1.414
                    elif u != 0:
                        cu = 1
                    elif v != 0:
                        cv = 1
                    sum += (2*cu*cv/N)*(img2[x,y]*cos(((2*x+1)*u*pi)/(2*N))*cos(((2*y+1)*v*pi)/(2*N)))
            img2[u,v] = sum
            sum = 0
    return img2
imgy2 = FDCT_for_gray(imgy)
'''
imgy = imgy - np.ones((8,8))*128
dct_img = cv2.dct(np.float32(imgy))
print(dct_img)
idct_img = cv2.idct(np.float32(dct_img))
print(idct_img)
#print(FDCT.iFDCT_for_gray(imgy2))
'''
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
'''
#print(FDCT.FDCT_for_gray(img2[0]))

