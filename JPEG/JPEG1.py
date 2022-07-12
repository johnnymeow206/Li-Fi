from PIL import Image
import numpy as np
from sympy import cos, pi

def rgb_to_y(img_array):
    R,G,B = img_array[0], img_array[1], img_array[2]
    return 0.299 * R + 0.587 * G + 0.114 * B
def rgb_to_Cb(img_array):
    R,G,B = img_array[0], img_array[1], img_array[2]
    return 0.1687 * R - 0.3313 * G + 0.5 * B
def rgb_to_Cr(img_array):
    R,G,B = img_array[0], img_array[1], img_array[2]
    return 0.5 * R - 0.4187 * G - 0.0813 * B

img2 = Image.open('lena_gray.bmp').convert('RGB')#圖片轉成RGB形式
img2 = np.array(img2) #變成RGB形式的矩陣
img2 = np.transpose(img2) #讓陣列由列變成行?
imgy = rgb_to_y(img2)
imgCb = rgb_to_Cb(img2)
imgCr = rgb_to_Cr(img2)
#print(imgy[:8,:8])
#FDCT
N = 8
imgy2 = imgy
imgCb2 = imgCb
imgCr2 = imgCr
for  x in range(8):    
    for y in range(8):
        if x == 0 and y == 0:
            cucv = 1/1.414
        else:
            cucv = 1
        imgy[x,y] = imgy[x,y] - 128
        imgy2[x,y] = (2*cucv/N)*(imgy[x,y]*cos(((2*x+1)*x*pi.evalf())/(2*N))*cos(((2*y+1)*y*pi.evalf())/(2*N)))
        imgCb[x,y] = imgCb[x,y] - 128
        imgCb2[x,y] = (2*cucv/N)*(imgCb[x,y]*cos(((2*x+1)*x*pi.evalf())/(2*N))*cos(((2*y+1)*y*pi.evalf())/(2*N)))
        imgCr[x,y] = imgCr[x,y] - 128
        imgCr2[x,y] = (2*cucv/N)*(imgCr[x,y]*cos(((2*x+1)*x*pi.evalf())/(2*N))*cos(((2*y+1)*y*pi.evalf())/(2*N)))
#quantization
Y =np.array([[16,11,10,16,24,40,51,61],
             [12,12,14,19,26,58,60,55],
             [14,13,16,24,40,57,69,56],
             [14,17,22,19,51,87,80,62],
             [18,22,37,56,68,109,103,77],
             [24,35,55,64,81,104,113,92],
             [49,64,78,87,103,121,120,101],
             [72,92,95,98,112,100,103,99]])
CbCr =np.array([[17,18,24,47,99,99,99,99],
                [18,21,16,66,99,99,99,99],
                [24,26,56,99,99,99,99,99],
                [47,66,99,99,99,99,99,99],
                [99,99,99,99,99,99,99,99],
                [99,99,99,99,99,99,99,99],
                [99,99,99,99,99,99,99,99],
                [99,99,99,99,99,99,99,99]])
imgy3 = imgy2
imgCb3 = imgCb2
imgCr3 = imgCr2
for x in range(8):
    for y in range(8):
        imgy3[x,y] = round(imgy2[x,y]/Y[x,y])
        imgCb3[x,y] = round(imgCb2[x,y]/CbCr[x,y])
        imgCr3[x,y] = round(imgCr2[x,y]/CbCr[x,y])
print(imgCb3[:8,:8])

