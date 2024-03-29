import numpy as np
from sympy import pi
import cv2
import Def
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

        ################################<<Zig-Zag>>#################################
        img3[i][j] = Def.zigzag(img3[i][j])
        #print(img3[i][j])

        ###################################<<RLE>>##################################
        img3[i][j] = Def.RLE_AC(img3[i][j])
        #print(img3[i][j])


