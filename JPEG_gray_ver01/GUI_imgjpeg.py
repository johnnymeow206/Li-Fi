
import Def, cv2, Def2
import numpy as np
import copy

class Img_JPEG():
    def __init__(self, FilePath, OutputFilename, Q_value):
        self.OutputFilename = OutputFilename
        img_input = cv2.imread(FilePath[0],0)
        img_shape = img_input.shape # 照片大小
        self.rows = img_shape[0]
        self.cols = img_shape[1]
        self.h = int(img_shape[0]/8) #高 切割數量
        self.w = int(img_shape[1]/8) #寬 切割數量
        self.channels = 1
        img_input=img_input.reshape(self.rows, self.cols, self.channels)
        img0 = np.transpose(img_input)
        self.JPEG_init(img0, Q_value)
    
    def JPEG_init(self, img0, Q_value):
        img1 = np.split(img0, self.h, axis=1)
        img3 = [[[[0 for k1 in range(self.w)] for k2 in range(self.w)] for k3 in range(self.w)] for k4 in range(self.w)]
        self.ImgAfterDCT = [[[[0 for k1 in range(self.w)] for k2 in range(self.w)] for k3 in range(self.w)] for k4 in range(self.w)]
        self.ImgAfterZigzag = [[[[0 for k1 in range(self.w)] for k2 in range(self.w)] for k3 in range(self.w)] for k4 in range(self.w)]
        for i in range(self.w):
            img2 = np.dsplit(img1[i], self.w)
            for j in range(self.w):
                img3[i][j] = img2[j]
        for i in range(self.h):
            for j in range(self.w):
                img4 = np.asmatrix(img3[i][j])
                img4 = img4.astype(np.float32)
                img4 -= 128*np.ones((8,8))
                img4 = Def.FDCT3(img4)
                self.ImgAfterDCT[i][j] = copy.deepcopy(img4)
        self.JPEG_ZigZag(Q_value)
        self.JPEG_remain(Q_value)
        self.temp_DCT = Def.combine_picture(self.ImgAfterDCT ,self.h ,self.w ,self.rows ,self.cols ,self.channels)
    
    def JPEG_DCT(self):
        cv2.imwrite(self.OutputFilename + "DCT.jpg" , self.temp_DCT)
    
    def JPEG_ZigZag(self, Q_value):
        temp_ZigZag = copy.deepcopy(self.ImgAfterDCT)
        for i in range(self.h):
            for j in range(self.w):
                temp_ZigZag[i][j] = Def.quan_try(temp_ZigZag[i][j], Q_value)
                temp_ZigZag[i][j] = np.round_(temp_ZigZag[i][j],0)
                temp_ZigZag[i][j] = Def.zigzag(temp_ZigZag[i][j])
        self.ImgAfterZigzag = temp_ZigZag
        temp_ZigZag = Def.combine_picture(temp_ZigZag ,self.h ,self.w ,self.rows ,self.cols ,self.channels)
        cv2.imwrite(self.OutputFilename + "Zigzag.jpg" ,temp_ZigZag)

    def JPEG_transmit(self):
        img3 = copy.deepcopy(self.ImgAfterZigzag)
        temp02 = 0
        for i in range(self.h):
            for j in range(self.w):
                img3[i][j] = Def.RLE_AC(img3[i][j])
                temp = img3[i][j][0] - temp02
                temp02 = img3[i][j][0]
                img3[i][j][0] = temp

                img3[i][j] = Def2.Huff_Y(img3[i][j])

            img3[i] = ''.join(img3[i])
        img3 = ''.join(img3)
        height = self.h*8
        width = self.w*8
        bin_height = Def2.bin_huff(height)
        bin_width = Def2.bin_huff(width)
        img3 = bin_height + bin_width + img3
        return img3


    def JPEG_remain(self, Q_value):
        temp_remain = copy.deepcopy(self.ImgAfterZigzag)
        for i in range(self.h):
            for j in range(self.w):
                temp_remain[i][j] = Def.RLE_AC(temp_remain[i][j])

                temp_remain[i][j] = Def.InvRLE_AC(temp_remain[i][j])
                temp_remain[i][j] = Def.izigzag(temp_remain[i][j])
                img5 = temp_remain[i][j]
                img5 = Def.iquan_try(img5, Q_value)
                img4 = np.asmatrix(img5)
                img4 = img4.astype(np.float32)
                img4 = Def.iFDCT3(img4)
                img4 += 128*np.ones((8,8))
                temp_remain[i][j] = img4
                temp_remain[i][j] = np.clip(temp_remain[i][j],0,255)
        temp_remain = Def.combine_picture(temp_remain ,self.h ,self.w ,self.rows ,self.cols ,self.channels)
        cv2.imwrite(self.OutputFilename + "R1.jpg",temp_remain)
