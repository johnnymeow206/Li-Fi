import numpy as np
from sympy import pi
import cv2
import Def
np.set_printoptions(threshold=65536)

rows=256
cols=256
channels =1
i = 0
w = 32

img=np.fromfile(r'lena', dtype='uint8')

img=img.reshape(rows, cols, channels)

img = np.transpose(img) 
img1 = np.split(img, w, axis=1)

img3 = [[[[0 for k1 in range(w)] for k2 in range(w)] for k3 in range(w)] for k4 in range(w)]


########################################<<矩陣分割>>#################################
for i in range(w):
    img2 = np.dsplit(img1[i], w)

    for j in range(w):
        img3[i][j] = img2[j]

for i in range(w):
    for j in range(w):
        
        ###################################<<DCT>>###################################
        img4 = np.asmatrix(img3[i][j])
        img4 = img4.astype(np.float32)
        img4 -= 128*np.ones((8,8))
        img4 = cv2.dct(img4)

        ##############################<<Quantization>>###############################
        img3[i][j] = img4
        img3[i][j] = Def.quan(img3[i][j])

        for k in range(8):
            for l in range(8):
                img3[i][j][k][l] = round(img3[i][j][k][l])

        ##############################<<IQuantization>>###############################
        img5 = img3[i][j]
        img5 = Def.iquan(img5)

        ###################################<<IDCT>>###################################
        img4 = np.asmatrix(img5)
        img4 = img4.astype(np.float32)
        img4 = cv2.idct(img4)
        img4 += 128*np.ones((8,8))
        img3[i][j] = img4

g = 32
img_merge = [[0 for k1 in range(8)] for k2 in range(32)]
for c in range(g):
    img_merge[c] = img3[c][0]
    b = 1
    for a in range(31):
        img_merge[c] = np.hstack((img_merge[c],img3[c][b]))
        b+=1

img_merge1 = img_merge[0]
e = 0
f = 1
for d in range(31):
    img_merge1 = np.vstack((img_merge1,img_merge[f]))
    e+=1 
    f+=1
img = np.transpose(img)
#print(img)
img_merge1 = np.transpose(img_merge1)
img_merge1 = img_merge1.astype(np.uint8)
img_merge1=img_merge1.reshape(rows, cols, channels)
print(img_merge1)
cv2.imshow('temp', img_merge1)
cv2.waitKey(0) 

'''
        ################################<<Zig-Zag>>#################################
        img3[i][j] = Def.zigzag(img3[i][j])

        ###################################<<RLE>>##################################
        img3[i][j] = Def.RLE_AC(img3[i][j])
        #print(img3[i][j])

        ################################<<iZig-Zag>>#################################
        img3[i][j] = Def.izigzag(img3[i][j])
'''
