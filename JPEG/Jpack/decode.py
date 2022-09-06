import Def
import Def2
import numpy as np

def decode(decode_img, w):
    img3 = [[[[0 for k1 in range(w)] for k2 in range(w)] for k3 in range(w)] for k4 in range(w)]
    
    inp_list = [[[[0 for k1 in range(w)] for k2 in range(w)] for k3 in range(w)] for k4 in range(w)]
    temp02 = 0
    #inp_list = decode_img
    #'''
            ###################################<<invHuffman>>##################################
    img5 = Def2.InvHuff(decode_img)

    o = 0
    for i in range(w):
        for j in range(w):
            inp_list[i][j] = img5[o]
            o+=1
    #'''
    for i in range(w):
        for j in range(w):
            ###################################<<invDPCM>>##################################
            temp01 = inp_list[j][i][0] + temp02
            inp_list[j][i][0] = temp01
            temp02 = inp_list[j][i][0]

            ###################################<<invRLE>>##################################
            img3[j][i] = Def.InvRLE_AC(inp_list[j][i])

            ################################<<iZig-Zag>>#################################
            img3[j][i] = Def.izigzag(img3[j][i])
          
            ##############################<<IQuantization>>###############################
            img5 = img3[j][i]
            img5 = Def.iquan(img5)
            #img5 = Def.iquan_try(img5,80)
            ###################################<<IDCT>>###################################
            img4 = np.asmatrix(img5)
            img4 = img4.astype(np.float32)
            #img4 = cv2.idct(img4)
            #img4 = FDCT.iFDCT_for_gray(img4)
            #img4 = Def.InvFDCT(img4)
            img4 = Def.iFDCT3(img4)
            img4 += 128*np.ones((8,8))
            img3[j][i] = img4
            img3[j][i] = np.clip(img3[j][i],0,255)
            
    return img3