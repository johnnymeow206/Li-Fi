
import cv2
from PIL import Image
import numpy as np
from sympy import cos, pi
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
imgy2 = FDCT.FDCT_for_gray(imgy)
print(imgy2)
print(FDCT.iFDCT_for_gray(imgy2))
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

