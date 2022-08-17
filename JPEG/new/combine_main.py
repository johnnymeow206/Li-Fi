import numpy as np
from sympy import pi
import cv2
import Def
import Def2
import FDCT
import FDCT_more
import time
import Huff_try
np.set_printoptions(threshold=np.inf)
start = time.time()

rows=256
cols=256
channels =1
i = 0
w = 32
t = 16

img=np.fromfile(r'lena', dtype='uint8')
img=img.reshape(rows, cols, channels)

#cv2.imshow('temp', img)
#cv2.waitKey(0) 
def encode(encode_img):
    img = np.transpose(encode_img) 
    img1 = np.split(img, w, axis=1)
    #print(img)
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
            #img4 = cv2.dct(img4)
            #img4 = FDCT.FDCT_for_gray(img4)
            #img4 = Def.FDCT(img4)
            img4 = FDCT_more.FDCT3(img4)

            #print(img3[11][11])
            ##############################<<Quantization>>###############################
            img3[i][j] = img4
            img3[i][j] = Def.quan(img3[i][j])
            #img3[i][j] = np.round_(img3[i][j],1)
            img3[i][j] = np.round_(img3[i][j],0)
            '''
            print(i,j)
            print(img3[i][j])
            
            for k in range(8):
                for l in range(8):
                    img3[i][j][k][l] = np.round_(img3[i][j][k][l],0)
            '''
            
            ################################<<Zig-Zag>>#################################
            img3[i][j] = Def.zigzag(img3[i][j])

            ###################################<<RLE>>##################################
            img3[i][j] = Def.RLE_AC(img3[i][j])
            
            ###################################<<DPCM>>##################################
            temp2 = 0
            temp = img3[j][i][0]-temp2
            temp2 = img3[j][i][0]
            img3[j][i][0] = temp
            '''
            ###################################<<Huffman>>##################################
            img3[i][j] = Def2.Huff1(img3[i][j])
        img3[i] = ''.join(img3[i])
    img3 = ''.join(img3)
    '''
    return img3

def decode(decode_img):
    img3 = [[[[0 for k1 in range(w)] for k2 in range(w)] for k3 in range(w)] for k4 in range(w)]
    
    inp_list = [[[[0 for k1 in range(w)] for k2 in range(w)] for k3 in range(w)] for k4 in range(w)]
    temp02 = 0
    '''
            ###################################<<invHuffman>>##################################
    img5 = Huff_try.InvHuff(decode_img)
    o = 0
    #img3 = np.reshape(img3,[32,32])
    for i in range(w):
        for j in range(w):
            inp_list[i][j] = img5[o]
            o+=1
            '''
    inp_list = decode_img 
    for i in range(w):
        for j in range(w):

            ###################################<<invDPCM>>##################################
            temp01 = inp_list[j][i][0] + temp02
            temp02 = inp_list[j][i][0]
            inp_list[j][i][0] = temp01

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
            img4 = FDCT_more.iFDCT3(img4)
            img4 += 128*np.ones((8,8))
            img3[i][j] = img4
            img3[i][j] = np.clip(img3[i][j],0,255)
    return img3

abc = encode(img)
bcd = decode(abc)
#print(bcd)

g = 32
img_merge = [[0 for k1 in range(8)] for k2 in range(32)]
for c in range(g):
    img_merge[c] = bcd[c][0]
    b = 1
    for a in range(31):
        img_merge[c] = np.hstack((img_merge[c],bcd[c][b]))
        b+=1

img_merge1 = img_merge[0]
e = 0
f = 1
for d in range(31):
    img_merge1 = np.vstack((img_merge1,img_merge[f]))
    e+=1 
    f+=1
img = np.transpose(img)
img_merge1 = np.transpose(img_merge1)
img_merge1 = img_merge1.astype(np.uint8)
img_merge1=img_merge1.reshape(rows, cols, channels)
cv2.imshow('temp', img_merge1)
cv2.waitKey(0) 

end = time.time()
print(format(end-start))


