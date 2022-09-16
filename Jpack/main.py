import numpy as np
import cv2
import encode
import decode
import hamming
import time

'''
w = 32
count = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
        21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
        31]
rows = 256
cols = 256
channels = 1

img=np.fromfile(r'lena', dtype='uint8')
img=img.reshape(rows, cols, channels)
'''
#img = cv2.imread("lena_color_256.tif",0)
img = cv2.imread("lena_gray_256.tif",0)
img_shape = img.shape # 照片大小
rows = img_shape[0]
cols = img_shape[1]
h = int(img_shape[0]/8) #高 切割數量
w = int(img_shape[1]/8) #寬 切割數量
channels = 1
img=img.reshape(rows, cols, channels)

encode_start = time.time()
abc = encode.encode(img,h, w)
#abc = hamming.hamming_encoding(abc)
encode_end = time.time()
#print(len(abc))

decode_start = time.time()
#abc = hamming.hamming_decoding(abc)
bcd = decode.decode(abc)
decode_end = time.time()

print("總運行時間:{}".format(decode_end - encode_start))
print("encode運行時間:{}".format(encode_end - encode_start))
print("decode運行時間:{}".format(decode_end - decode_start))
decode.combine_picture(bcd,h ,w ,rows, cols, channels) #組合並顯示圖片
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

