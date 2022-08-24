import numpy as np
from sympy import pi
import cv2
import Def
import Def2
import time
import copy
start = time.time()
rows=256
cols=256
channels =1
i = 0
w = 32

count = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
        21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
        31]


img=np.fromfile(r'lena', dtype='uint8')
img=img.reshape(rows, cols, channels)

img = np.transpose(img) 
img1 = np.split(img, w, axis=1)

img3 = [[[[0 for k1 in range(w)] for k2 in range(w)] for k3 in range(w)] for k4 in range(w)]

for i in range(w):
    img2 = np.dsplit(img1[i], w)

    for j in range(w):
        img3[i][j] = img2[j]
#img3 = resized_image.astype(np.float32)


for i in range(w):
    for j in range(w):
        img4 = np.asmatrix(img3[i][j])
        img4 = img4.astype(np.float32)
        img4 -= 128*np.ones((8,8))
        img4 = cv2.dct(img4)

        img3[i][j] = img4
        img3[i][j] = Def.quan(img3[i][j])

        for k in range(8):
            for l in range(8):
                img3[i][j][k][l] = round(img3[i][j][k][l])

        img3[i][j] = Def.zigzag(img3[i][j])
        img3[i][j] = Def.RLE_AC(img3[i][j])
        #print(img3[i][j])

temp0000 = copy.deepcopy(img3)

########DPCM
temp02 = 0
for i in range(w):
    for j in range(w):
        temp = img3[j][i][0] - temp02
        temp02 = img3[j][i][0]
        img3[j][i][0] = temp

        #print(j,i)
        #print('temp02 =', temp02)
        #print('After:',img3[j][i])


########Huff+combin
#'''
for i in range(w):
    for j in range(w):
        img3[i][j] = Def2.Huff(img3[i][j])
    img3[i] = ''.join(img3[i])
img3 = ''.join(img3)
#'''
def decode(decode_img):
    w = 32
    img3 = [[[[0 for k1 in range(w)] for k2 in range(w)] for k3 in range(w)] for k4 in range(w)]
    
    inp_list = [[[[0 for k1 in range(w)] for k2 in range(w)] for k3 in range(w)] for k4 in range(w)]
    temp02 = 0
    #inp_list = decode_img
    #'''
            ###################################<<invHuffman>>##################################
    img5 = Def2.InvHuff(decode_img)

    o = 0
    #img3 = np.reshape(img3,[32,32])
    for i in range(w):
        for j in range(w):
            inp_list[i][j] = img5[o]
            o+=1
    #'''
    for i in range(w):
        for j in range(w):
            ###################################<<invDPCM>>##################################
            #print(j,i)
            #print('temp02 =', temp02)
            #print('Before:',inp_list[j][i])

            temp01 = inp_list[j][i][0] + temp02
            inp_list[j][i][0] = temp01
            temp02 = inp_list[j][i][0]
            #print(j, i)
            #Def.error_check(temp0000[j][i], inp_list[j][i])
    #print(inp_list[10][0])
    
            #print('After:',inp_list[i][j])
            ###################################<<invRLE>>##################################
            img3[j][i] = Def.InvRLE_AC(inp_list[j][i])

            ################################<<iZig-Zag>>#################################
            img3[j][i] = Def.izigzag(img3[j][i])
          
            ##############################<<IQuantization>>###############################
            img5 = img3[j][i]
            img5 = Def.iquan(img5)
            
            ###################################<<IDCT>>###################################
            img4 = np.asmatrix(img5)
            img4 = img4.astype(np.float32)
            #img4 = cv2.idct(img4)
            #img4 = FDCT.iFDCT_for_gray(img4)
            #img4 = Def.InvFDCT(img4)
            img4 = Def.iFDCT(img4)
            img4 += 128*np.ones((8,8))
            img3[j][i] = img4
            img3[j][i] = np.clip(img3[j][i],0,255)
            
    return img3

#print(abc)
bcd = decode(img3)
end = time.time()
print(format(end-start))


img_merge = [[0 for k1 in range(8)] for k2 in range(w)]
for c in range(w):
    img_merge[c] = bcd[c][0]
    b = 1
    for a in range(w-1):
        img_merge[c] = np.hstack((img_merge[c],bcd[c][b]))
        b+=1

img_merge1 = img_merge[0]
e = 0
f = 1
for d in range(w-1):
    img_merge1 = np.vstack((img_merge1,img_merge[f]))
    e+=1 
    f+=1
img = np.transpose(img)
img_merge1 = np.transpose(img_merge1)
img_merge1 = img_merge1.astype(np.uint8)
img_merge1=img_merge1.reshape(rows, cols, channels)
cv2.imshow('temp', img_merge1)
cv2.waitKey(0) 

'''
########snake diff

pre_last = 0
for i in range(w):
    diff = []

    for j in range(w):
        if j != 0:
            diff.append(img3[count[j]][i][0]-img3[count[j-1]][i][0])
 
        else:
            diff.append(img3[count[j]][i][0]-pre_last)

    pre_last = img3[count[31]][i][0]
    for j in range(w):
        img3[count[j]][i][0] = diff[j]
        #print(img3[j][i])
    
    if i%2 == 0:
        count = sorted(count)
    else:
        count = sorted(count,reverse = True)
'''