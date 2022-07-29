
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


imgy = imgy - np.ones((8,8))*128
dct_img = cv2.dct(np.float32(imgy))
print(dct_img)
idct_img = cv2.idct(np.float32(dct_img))
print(idct_img)

