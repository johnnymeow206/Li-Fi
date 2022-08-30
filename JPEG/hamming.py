import numpy as np
from sympy import pi
import cv2
import Def2
import hamming

import time

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


encode_start = time.time()
abc = Def2.encode(img, w)
abc = hamming.hamming_encoding(abc)
encode_end = time.time()
#print(abc)

decode_start = time.time()
abc = hamming.hamming_decoding(abc)
bcd = Def2.decode(abc, w)
decode_end = time.time()

print("總運行時間:{}".format(decode_end - encode_start))
print("encode運行時間:{}".format(encode_end - encode_start))
print("decode運行時間:{}".format(decode_end - decode_start))


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
