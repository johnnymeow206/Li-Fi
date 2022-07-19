from PIL import Image
import numpy as np
from sympy import cos, pi
import FDCT
import cv2
import Def

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
img2y = np.asmatrix(img2[0])

img2y = img2y - np.ones((8,8))*128
dct_img = cv2.dct(img2y)
print(dct_img)
'''
idct_img = cv2.idct(dct_img)
print(idct_img)
'''
Quan_img = Def.quan(dct_img)
for x in range(8):
    for y in range(8):
        Quan_img[x,y] = round(Quan_img[x,y])
print(Quan_img)
zig = np.asmatrix(Quan_img)
Zig_img = Def.zigzag(zig)
print(Zig_img)

temp = np.zeros([64,2])
a = b = c = 0
while a < 64:
    if Zig_img[a]!=0:
        temp[b] = [0,Zig_img[a]]
        if Zig_img[a-1]==0:
            temp[b] = [c,Zig_img[a]]
            c = 0
        b+=1
    elif Zig_img[a]==0:
        c+=1
    a+=1
RLE = np.resize(temp,(b,2))
print(temp)



