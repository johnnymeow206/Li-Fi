import numpy as np
from sympy import pi
import cv2
import Def
import Def2
import time
import Def_for_Huff
np.set_printoptions(threshold=np.inf)

rows=512
cols=512
channels =1
w = 64
img = cv2.imread("lena_gray_512.tif",0)
img=img.reshape(rows, cols, channels)
'''
rows=256
cols=256
channels =1
w = 64
i = 0
t = 16

img=np.fromfile(r'lena', dtype='uint8')
img=img.reshape(rows, cols, channels)
'''
#cv2.imshow('image', img)
#cv2.waitKey(0) 
def encode(encode_img):
    img = np.transpose(encode_img) 
    img1 = np.split(img, w, axis=1)
    #print(img)
    img3 = [[[[0 for k1 in range(w)] for k2 in range(w)] for k3 in range(w)] for k4 in range(w)]
    temp2 = 0
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
            #img4 = cv2.dct(img4)
            #img4 = FDCT.FDCT_for_gray(img4)
            #img4 = Def.FDCT(img4)
            img4 = Def.FDCT3(img4)

            ##############################<<Quantization>>###############################
            img3[i][j] = img4
            img3[i][j] = Def.quan(img3[i][j])
            #img3[i][j] = np.round_(img3[i][j],1)
            img3[i][j] = np.round_(img3[i][j],0)
            
            ################################<<Zig-Zag>>#################################
            img3[i][j] = Def.zigzag(img3[i][j])

            ###################################<<RLE>>##################################
            img3[i][j] = Def.RLE_AC(img3[i][j])
            #print(i,j)
            #print(img3[i][j])
            ###################################<<DPCM>>##################################
            temp = img3[i][j][0]-temp2
            temp2 = img3[i][j][0]
            img3[i][j][0] = temp
    #'''
            ###################################<<Huffman>>##################################
            img3[i][j] = Def_for_Huff.Huff1(img3[i][j])
            #img3[i][j] = Def2.Huff(img3[i][j])
            #print(img3[i][j])
        img3[i] = ''.join(img3[i])
    img3 = ''.join(img3)
    #'''
    return img3

def decode(decode_img):
    img3 = [[[[0 for k1 in range(w)] for k2 in range(w)] for k3 in range(w)] for k4 in range(w)]
    
    inp_list = [[[[0 for k1 in range(w)] for k2 in range(w)] for k3 in range(w)] for k4 in range(w)]
    temp02 = 0
    #inp_list = decode_img
    #'''
            ###################################<<invHuffman>>##################################
    img5 = Def_for_Huff.InvHuff1(decode_img, w)
    #img5 = Def2.InvHuff(decode_img)
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
            #print(i,j)
            #print('temp02 =', temp02)
            #print('Before:',inp_list[i][j])

            temp01 = inp_list[i][j][0] + temp02
            inp_list[i][j][0] = temp01
            temp02 = inp_list[i][j][0]
            
            #print('After:',inp_list[i][j])
            ###################################<<invRLE>>##################################
            img3[i][j] = Def.InvRLE_AC(inp_list[i][j])

            ################################<<iZig-Zag>>#################################
            img3[i][j] = Def.izigzag(img3[i][j])
          
            ##############################<<IQuantization>>###############################
            img5 = img3[i][j]
            img5 = Def.iquan(img5)
            
            ###################################<<IDCT>>###################################
            img4 = np.asmatrix(img5)
            img4 = img4.astype(np.float32)
            #img4 = cv2.idct(img4)
            #img4 = FDCT.iFDCT_for_gray(img4)
            #img4 = Def.InvFDCT(img4)
            img4 = Def.iFDCT3(img4)
            img4 += 128*np.ones((8,8))
            img3[i][j] = img4
            img3[i][j] = np.clip(img3[i][j],0,255)
            
    return img3
start = time.time()
abc = encode(img)

#print(abc)
bcd = decode(abc)
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


