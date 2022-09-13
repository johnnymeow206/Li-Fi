import numpy as np
import cv2
import Def
import Def2
import copy
img = cv2.imread("lena_color_256.tif",0)
#img = cv2.imread("lena_gray_256.tif",0)
img_shape = img.shape # 照片大小
rows = img_shape[0]
cols = img_shape[1]
h = int(img_shape[0]/8) #高 切割數量
w = int(img_shape[1]/8) #寬 切割數量
channels = 1
img=img.reshape(rows, cols, channels)
###############encode###################
img = np.transpose(img) 
img1 = np.split(img, h, axis=1) #水平切
img3 = [[[[0 for k1 in range(w)] for k2 in range(w)] for k3 in range(w)] for k4 in range(w)]
inp_list = [[[[0 for k1 in range(w)] for k2 in range(w)] for k3 in range(w)] for k4 in range(w)]
temp02 = 0
for i in range(w):#每一片水平的再縱切
    img2 = np.dsplit(img1[i], w)
    for j in range(w):#每一格再丟入img3
        img3[i][j] = img2[j]
#img3 = resized_image.astype(np.float32)
for i in range(h):
    for j in range(w):
        img4 = np.asmatrix(img3[i][j])
        img4 = img4.astype(np.float32)
        img4 -= 128*np.ones((8,8))
        img4 = Def.FDCT3(img4)

        img3[i][j] = img4
        #img3[i][j] = Def.quan(img3[i][j])
        img3[i][j] = Def.quan_try(img3[i][j], 62)
        
        img3[i][j] = np.round_(img3[i][j],0)
        img3[i][j] = Def.zigzag(img3[i][j])

        img3[i][j] = Def.RLE_AC(img3[i][j])
######################DPCM#####################
        temp = img3[i][j][0] - temp02
        temp02 = img3[i][j][0]
        img3[i][j][0] = temp
        #print(i,j)
        #print(img3[i][j])
img6 = copy.deepcopy(img3)
#print(img6[0][0])
for i in range(h):
    for j in range(w):
##################Huff+combine###################
        img3[i][j] = Def2.Huff(img3[i][j])
    img3[i] = ''.join(img3[i])
img3 = ''.join(img3)
print(img3)
###############decode#################
hihi = Def2.ibin_huff(img3)
img_shape = hihi[0]
n = hihi[1]

###################################<<invHuffman>>##################################
img5 = Def2.InvHuff(img3,h,w,n)
#print(img5)
o = 0
for i in range(h):
    for j in range(w):
        inp_list[i][j] = img5[o]
        o+=1
#print(inp_list[0][0])

Def.error_check(img6, inp_list)

