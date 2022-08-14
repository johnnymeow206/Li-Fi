import numpy as np
from sympy import pi
import cv2
import Def
import Def2
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

########DIFF
temp02 = 0
for i in range(w):
    for j in range(w):
        temp = img3[j][i][0] - temp02
        temp02 = img3[j][i][0]
        img3[j][i][0] = temp
########Huff+combin
for i in range(w):
    for j in range(w):
        img3[i][j] = Def2.Huff(img3[i][j])
    img3[i] = ''.join(img3[i])
img3 = ''.join(img3)
print(img3)


'''
#######invDIFF(假設已排序好)
#inp_list 為輸入矩陣
temp02 = 0
for i in range(w):
    for j in range(w):
        temp01 = inp_list[j][i][0] + temp02
        temp02 = inp_list[j][i][0]
        inp_list[j][i][0] = temp

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

