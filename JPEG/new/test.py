
import cv2
from PIL import Image
import numpy as np
from sympy import cos, pi
import FDCT

img = np.zeros((500,500,3), dtype='uint8')   # 快速產生 500x500，每個項目為 [0,0,0] 的三維陣列
img[150:350, 150:350] = [0,0,255]  # 將中間 200x200 的每個項目內容，改為 [0,0,255]
cv2.imwrite('oxxostudio.jpg', img)       # 存成 jpg
cv2.imshow('oxxostudio', img)
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

