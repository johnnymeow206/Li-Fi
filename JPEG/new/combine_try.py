
import numpy as np
from sympy import pi
import cv2
import Def
import Def2
import combine_main
import time
import Def_for_Huff
np.set_printoptions(threshold=np.inf)

rows=256
cols=256
channels =1
i = 0
w = 32
t = 16

img=np.fromfile(r'lena', dtype='uint8')
img=img.reshape(rows, cols, channels)

abc = combine_main.encode(img)

inp_list = [[[[0 for k1 in range(w)] for k2 in range(w)] for k3 in range(w)] for k4 in range(w)]
img3 = [[[[0 for k1 in range(w)] for k2 in range(w)] for k3 in range(w)] for k4 in range(w)]
temp02 = 0
        ###################################<<invHuffman>>##################################
img5 = Def_for_Huff.InvHuff1(abc)
o = 0
#img3 = np.reshape(img3,[32,32])
for i in range(w):
    for j in range(w):
        inp_list[i][j] = img5[o]
        o+=1
for i in range(w):
    for j in range(w):
        ###################################<<invDPCM>>##################################
        temp01 = inp_list[i][j][0] + temp02
        temp02 = inp_list[i][j][0]
        inp_list[i][j][0] = temp01

        ###################################<<invRLE>>##################################
        img3[i][j] = Def.InvRLE_AC(inp_list[i][j])

        ################################<<iZig-Zag>>#################################
        img3[i][j] = Def.izigzag(img3[i][j])

        ##############################<<IQuantization>>###############################
        img6 = img3[i][j]
        img6 = Def.iquan(img6)
      
        ###################################<<IDCT>>###################################
        img4 = np.asmatrix(img6)
        img4 = img4.astype(np.float32)
        #img4 = cv2.idct(img4)
        #img4 = FDCT.iFDCT_for_gray(img4)
        #img4 = Def.InvFDCT(img4)
        img4 = Def.iFDCT3(img4)
        img4 += 128*np.ones((8,8))
        img3[i][j] = img4
        img3[i][j] = np.clip(img3[i][j],0,255)
        print(i,j)
        print(img3[i][j])
