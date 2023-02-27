import Def
import numpy as np
import copy

DC_Huff = ['00', '010', '011', '100', '101', '110', '1110', '11110', '111110', '1111110', '11111110', '111111110' ]

AC_Huff = [['00','01' ,'100', '1011', '11010', '1111000', '11111000', '1111110110', '1111111110000010', '1111111110000011'],
           ['1100', '11011', '1111001', '111110110', '11111110110', '1111111110000100', '1111111110000101', '1111111110000110', '1111111110000111', '1111111110001000'],
           ['11100', '11111001', '1111110111', '111111110100', '1111111110001001', '1111111110001010', '1111111110001011', '1111111110001100', '1111111110001101', '1111111110001110'],
           ['111010', '111110111', '111111110101', '1111111110001111', '1111111110010000', '1111111110010001', '1111111110010010', '1111111110010011', '1111111110010100', '1111111110010101'],
           ['111011', '1111111000', '1111111110010110', '1111111110010111', '1111111110011000', '1111111110011001', '1111111110011010', '1111111110011011', '1111111110011100', '1111111110011101'],
           ['1111010', '11111110111', '1111111110011110', '1111111110011111', '1111111110100000', '1111111110100001', '1111111110100010', '1111111110100011', '1111111110100100', '1111111110100101'],
           ['1111011', '111111110110', '1111111110100110', '1111111110100111', '1111111110101000', '1111111110101001', '1111111110101010', '1111111110101011', '1111111110101100', '1111111110101101'],
           ['11111010', '111111110111', '1111111110101110', '1111111110101111', '1111111110110000', '1111111110110001', '1111111110110010', '1111111110110011', '1111111110110100', '1111111110110101'],
           ['111111000', '111111111000000', '1111111110110110', '1111111110110111', '1111111110111000', '1111111110111001', '1111111110111010', '1111111110111011', '1111111110111100', '1111111110111101'],
           ['111111001', '1111111110111110', '1111111110111111', '1111111111000000', '1111111111000001', '1111111111000010', '1111111111000011', '1111111111000100', '1111111111000101', '1111111111000110'],
           ['111111010', '1111111111000111', '1111111111001000', '1111111111001001', '1111111111001010', '1111111111001011', '1111111111001100', '1111111111001101', '1111111111001110', '1111111111001111'],
           ['1111111001', '1111111111010000', '1111111111010001', '1111111111010010', '1111111111010011', '1111111111010100', '1111111111010101', '1111111111010110', '1111111111010111', '1111111111011000'],
           ['1111111010', '1111111111011001', '1111111111011010', '1111111111011011', '1111111111011100', '1111111111011101', '1111111111011110', '1111111111011111', '1111111111100000', '1111111111100001'],
           ['11111111000', '1111111111100010', '1111111111100011', '1111111111100100', '1111111111100101', '1111111111100110', ' 1111111111100111', '1111111111101000', '1111111111101001', '1111111111101010'],
           ['1111111111101011', '1111111111101100', '1111111111101101', '1111111111101110', '1111111111101111', '1111111111110000', '1111111111110001', '1111111111110010', '1111111111110011', '1111111111110100'],
           ['1111111111110101', '1111111111110110', '1111111111110111', '1111111111111000', '1111111111111001', '1111111111111010', '1111111111111011', '1111111111111100', '1111111111111101', '1111111111111110']]

           #0/0(EOB) 方便起見已移至最後一項'1010'
           #F/0 已移至倒數第二項,'11111111001'

iAC_Huff = ['00','01','100','1010','1011','1100','11010','11011','11100','111010','111011','1111000','1111001','1111010','1111011','11111000',
            '11111001','11111010','111110110','111110111','111111000','111111001','111111010','1111110110','1111110111','1111111000','1111111001','1111111010','11111110110','11111110111','11111111000','11111111001',
            '111111110100','111111110101','111111110110','111111110111','111111111000000','1111111110000010', '1111111110000011','1111111110000100', '1111111110000101', '1111111110000110', '1111111110000111', '1111111110001000',
            '1111111110001001', '1111111110001010', '1111111110001011', '1111111110001100', '1111111110001101', '1111111110001110','1111111110001111', '1111111110010000', '1111111110010001', '1111111110010010', '1111111110010011',
            '1111111110010100', '1111111110010101','1111111110010110', '1111111110010111', '1111111110011000', '1111111110011001', '1111111110011010', '1111111110011011', '1111111110011100', '1111111110011101',
            '1111111110011110', '1111111110011111', '1111111110100000', '1111111110100001', '1111111110100010', '1111111110100011', '1111111110100100', '1111111110100101','1111111110100110', '1111111110100111', '1111111110101000', 
            '1111111110101001', '1111111110101010', '1111111110101011', '1111111110101100', '1111111110101101','1111111110101110', '1111111110101111', '1111111110110000', '1111111110110001', '1111111110110010', '1111111110110011', 
            '1111111110110100', '1111111110110101','1111111110110110', '1111111110110111', '1111111110111000', '1111111110111001', '1111111110111010', '1111111110111011', '1111111110111100', '1111111110111101',
            '1111111110111110', '1111111110111111', '1111111111000000', '1111111111000001', '1111111111000010', '1111111111000011', '1111111111000100', '1111111111000101', '1111111111000110',
            '1111111111000111', '1111111111001000', '1111111111001001', '1111111111001010', '1111111111001011', '1111111111001100', '1111111111001101', '1111111111001110', '1111111111001111',
            '1111111111010000', '1111111111010001', '1111111111010010', '1111111111010011', '1111111111010100', '1111111111010101', '1111111111010110', '1111111111010111', '1111111111011000',
            '1111111111011001', '1111111111011010', '1111111111011011', '1111111111011100', '1111111111011101', '1111111111011110', '1111111111011111', '1111111111100000', '1111111111100001',
            '1111111111100010', '1111111111100011', '1111111111100100', '1111111111100101', '1111111111100110', ' 1111111111100111', '1111111111101000', '1111111111101001', '1111111111101010',
            '1111111111101011', '1111111111101100', '1111111111101101', '1111111111101110', '1111111111101111', '1111111111110000', '1111111111110001', '1111111111110010', '1111111111110011', '1111111111110100',
            '1111111111110101', '1111111111110110', '1111111111110111', '1111111111111000', '1111111111111001', '1111111111111010', '1111111111111011', '1111111111111100', '1111111111111101', '1111111111111110']
iRLE_code = [[0,1] ,[0,2] ,[0,3]  ,[0,0] ,[0,4]  ,[1,1] ,[0,5] ,[1,2]  ,[2,1] ,[3,1] ,[4,1] ,[0,6]  ,[1,3] ,[5,1]  ,[6,1] ,[0,7] ,
            [2,2] ,[7,1] ,[1,4]  ,[3,2] ,[8,1]  ,[9,1] ,[10,1],[0,8]  ,[2,3] ,[4,2] ,[11,1],[12,1] ,[1,5] ,[5,2]  ,[13,1],[15,0],
            [2,4] ,[3,3] ,[6,2]  ,[7,2] ,[8,2]  ,[0,9] ,[0,10],[1,6]  ,[1,7] ,[1,8] ,[1,9] ,[1,10] ,[2,5] ,[2,6]  ,[2,7] ,[2,8] ,
            [2,9] ,[2,10],[3,4]  ,[3,5] ,[3,6]  ,[3,7] ,[3,8] ,[3,9]  ,[3,10],[4,3] ,[4,4] ,[4,5]  ,[4,6] ,[4,7]  ,[4,8] ,[4,9] ,
            [4,10],[5,3] ,[5,4]  ,[5,5] ,[5,6]  ,[5,7] ,[5,8] ,[5,9]  ,[5,10],[6,3] ,[3,4] ,[6,5]  ,[6,6] ,[6,7]  ,[6,8] ,[6,9] ,
            [6,10],[7,3] ,[7,4]  ,[7,5] ,[7,6]  ,[7,7] ,[7,8] ,[7,9]  ,[7,10],[8,3] ,[8,4] ,[8,5]  ,[8,6] ,[8,7]  ,[8,8] ,[8,9] ,
            [8,10],[9,2] ,[9,3]  ,[9,4] ,[9,5]  ,[9,6] ,[9,7] ,[9,8]  ,[9,9] ,[9,10],[10,2],[10,3] ,[10,4],[10,5] ,[10,6],[10,7],
            [10,8],[10,9],[10,10],[11,2],[11,3] ,[11,4],[11,5],[11,6] ,[11,7],[11,8],[11,9],[11,10],[12,2],[12,3] ,[12,4],[12,5],
            [12,6],[12,7],[12,8] ,[12,9],[12,10],[13,2],[13,3],[13,4] ,[13,5],[13,6],[13,7],[13,8] ,[13,9],[13,10],[14,1],[14,2],
            [14,3],[14,4],[14,5] ,[14,6],[14,7] ,[14,8],[14,9],[14,10],[15,1],[15,2],[15,3],[15,4] ,[15,5],[15,6] ,[15,7],[15,8],
            [15,9],[15,10]]

AC_cbcr=[
        ['01','100','1010','11000','11001','111000','1111000','111110100','1111110110','111111110100'],
        ['1011','111001','11110110','111110101','11111110110','111111110101','1111111110001000','1111111110001001','1111111110001010','1111111110001011'],
        ['11010','11110111','1111110111','111111110110','111111111000010','1111111110001100','1111111110001101','1111111110001110','1111111110001111','1111111110010000'],
        ['11011','11111000','1111111000','111111110111','1111111110010001','1111111110010010','1111111110010011','1111111110010100','1111111110010101','1111111110010110'],
        ['111010','111110110','1111111110010111','1111111110011000','1111111110011001','1111111110011010','1111111110011011','1111111110011100','1111111110011101','1111111110011110'],
        ['111011','1111111001','1111111110011111','1111111110100000','1111111110100001','1111111110100010','1111111110100011','1111111110100100','1111111110100101','1111111110100110'],
        ['1111001','11111110111','1111111110100111','1111111110101000','1111111110101001','1111111110101010','1111111110101011','1111111110101100','1111111110101101','1111111110101110'],
        ['1111010','11111111000','1111111110101111','1111111110110000','1111111110110001','1111111110110010','1111111110110011','1111111110110100','1111111110110101','1111111110110110'],
        ['11111001','1111111110110111','1111111110111000','1111111110110111','1111111110111000','1111111110111001','1111111110111010','1111111110111011','1111111110111100','1111111110111101'],
        ['111111001','1111111110111110','1111111110111111','1111111110111001','1111111110111010','1111111110111011','1111111110111100','1111111110111101','1111111110111110','1111111110111111'],
        ['111110111','1111111111000000','1111111111000001','1111111111000010','1111111111000011','1111111111000100','1111111111000101','1111111111000110','1111111111000111','1111111111001000'],
        ['111111001','1111111111010010','1111111111010011','1111111111010100','1111111111010101','1111111111010110','1111111111010111','1111111111011000','1111111111011001','1111111111011010'],
        ['111111010','1111111111011011','1111111111011100','1111111111011101','1111111111011110','1111111111011111','1111111111100000','1111111111100001','1111111111100010','1111111111100011'],
        ['11111111001','1111111111100100','1111111111100101','1111111111100110','1111111111100111','1111111111101000','1111111111101001','1111111111101010','1111111111101011','1111111111101100'],
        ['11111111100000','1111111111101101','1111111111101110','1111111111101111','1111111111110000','1111111111110001','1111111111110010','1111111111110011','1111111111110100','1111111111110101'],
        ['111111111000011','1111111111110110','1111111111110111','1111111111111000','1111111111111001','1111111111111010','1111111111111011','1111111111111100','1111111111111101','1111111111111110']]



def int_to_bin(k):
    f = k
    f = int(f)
    if f < 0 :
        f = abs(f)
        f = format(f, 'b')
        f = ''.join('1' if x == '0' else '0' for x in f)
        
    else:
        f = format(f, 'b') 
    return f
def bin_to_int(list1):
    if list1[0] != '0':
        list1 = int(list1, 2)
    else:
        list1 = ''.join('1' if x == '0' else '0' for x in list1)
        list1 = int(list1, 2)
        list1 *= -1
    return list1

def Huff(array1):
    temp = array1
    diff = temp[0]
    if diff == 0:
        temp[0] =  DC_Huff[0]
    else:
        diff = int_to_bin(diff)
        temp[0] =  DC_Huff[len(diff)] + diff
    i = 1
    ff00 = 1
    while ff00 < 64:
        if temp[i] == [15,0]:     #ZRL detect
            temp[i] = '11111111001'
            ff00 += 16
            i += 1
            if ff00 == 64:
                temp[i]='1010'
                
        elif temp[i][0] == 'E':   #EOB detect
            temp[i] = '1010'
            ff00 = 64
        else:                     #normal AC detect 
            ff00 += temp[i][0] + 1
            temp02 = int_to_bin(temp[i][1])
            temp[i][1] = len(temp02)
            temp[i] = AC_Huff[temp[i][0]][temp[i][1]-1] + temp02
            i += 1
    return ''.join(temp)

#print(Huff([20, [0, 2], [0, 1], [2, 1], 'EOB']))

def DC_check(inp1):
    list001 = inp1
    for ff01 in range(12):
        list002 = list001[0:len(DC_Huff[ff01])]
        if list002 == DC_Huff[ff01]:
            return ff01     #DC的長度
    
def AC_check(inp1):
    list001 = inp1
    for ff01 in range(162):     
        list002 = list001[0:len(iAC_Huff[ff01])]
        if list002 == iAC_Huff[ff01]:
            return ff01     #回傳幾個零,後有幾位數

def AC_CbCr_check(inp1):   #exhaustive search
    list001 = inp1
    for ff01 in range(10): 
        for ff02 in range(10):     
            list002 = list001[0:len(AC_cbcr[ff01][ff02])]
            if list002 == AC_cbcr[ff01][ff02]:
                return [ff01, ff02+1]#從1開始數

def bin_huff(array1):
    temp = array1
    temp = int_to_bin(temp)
    temp =  DC_Huff[len(temp)] + temp
    return temp  
def ibin_huff(input1):
    now = 0
    temp01 = []
    for a in range(2):
        TEMP00 = input1[now:now+9]
        diff_length = DC_check(TEMP00)
        now += len(DC_Huff[diff_length])
        temp02 = input1[now:now+diff_length]
        now += len(temp02)
        temp02 = bin_to_int(temp02)
        temp01.append(temp02)
    return temp01, now
def InvHuff(inp,h,w,n):   #整體運行
    piece_size = h*w
    now = n
    input1 = inp
    out_list = []

    for i in range(piece_size):
        ##################DC
        TEMP00 = input1[now:now+9]
        #print(i)
        #print(TEMP00)
        if TEMP00 != '':
            temp01 = []
            diff_length = DC_check(TEMP00)
            now += len(DC_Huff[diff_length])
            if diff_length == 0:
                temp01.append(0)
            else:
                temp02 = input1[now:now+diff_length]
                now += len(temp02)
                temp02 = bin_to_int(temp02)
                temp01.append(temp02)
            #print(now- tttt)
            ####################AC
            code_length = 1
            while code_length < 64:
                TEMP00 = input1[now:now+16]
                zero_and_length = AC_check(TEMP00) 
                #print(TEMP00)
                #print(zero_and_length)
                if zero_and_length == 3:
                    code_length = 64
                    temp01.append('EOB')
                    now += 4
                elif zero_and_length == 31:
                    code_length += 16
                    temp01.append([15,0])
                    now += 11
                else:
                    code_length += (iRLE_code[zero_and_length][0]) 
                    now += len(iAC_Huff[zero_and_length])
                    temp02 = input1[now:now+iRLE_code[zero_and_length][1]]
                    code_length += 1
                    now += len(temp02)
                    temp02 = bin_to_int(temp02)
                    temp02 = [iRLE_code[zero_and_length][0], temp02]
                    temp01.append(temp02)
            #print(i)
            #print(temp01)        
        else:
            print(i)
        out_list.append(temp01) 
    return out_list

def Huff_Y(array1):
    temp = array1
    diff = temp[0]
    if diff == 0:
        temp[0] =  DC_Huff[0]
    else:
        diff = int_to_bin(diff)
        temp[0] =  DC_Huff[len(diff)] + diff
    i = 1
    ff00 = 1
    while ff00 < 64:
        if temp[i] == [15,0]:     #ZRL detect
            temp[i] = '11111111001'
            ff00 += 16
            i += 1
            if ff00 == 64:
                temp[i]='1010'
                
        elif temp[i][0] == 'E':   #EOB detect
            temp[i] = '1010'
            ff00 = 64
        else:                     #normal AC detect 
            ff00 += temp[i][0] + 1
            temp02 = int_to_bin(temp[i][1])
            temp[i][1] = len(temp02)
            temp[i] = AC_Huff[temp[i][0]][temp[i][1]-1] + temp02
            i += 1
    return ''.join(temp)

def Huff_CbCr(array1):
    temp = array1
    diff = temp[0]
    if diff == 0:
        temp[0] =  DC_Huff[0]
    else:
        diff = int_to_bin(diff)
        temp[0] =  DC_Huff[len(diff)] + diff
    i = 1
    ff00 = 1
    while ff00 < 64:
        if temp[i] == [15,0]:     #ZRL detect
            temp[i] = '1111111010'
            ff00 += 16
            i += 1
            if ff00 == 64:
                temp[i]='00'
                
        elif temp[i][0] == 'E':   #EOB detect
            temp[i] = '00'
            ff00 = 64
        else:                     #normal AC detect 
            ff00 += temp[i][0] + 1
            temp02 = int_to_bin(temp[i][1])
            temp[i][1] = len(temp02)
            temp[i] = AC_cbcr[temp[i][0]][temp[i][1]-1] + temp02
            i += 1
    return ''.join(temp)

def InvHuff_CbCr(inp,h,w):   #整體運行
    piece_size = h*w
    now = 0
    input1 = inp
    out_list = []
    for i in range(piece_size):
        ##################DC
        TEMP00 = input1[now:now+9]
        temp01 = []
        diff_length = DC_check(TEMP00)
        now += len(DC_Huff[diff_length])
        if diff_length == 0:
            temp01.append(0)
        else:
            temp02 = input1[now:now+diff_length]
            now += len(temp02)
            temp02 = bin_to_int(temp02)
            temp01.append(temp02)
        #print(now- tttt)
        ####################AC
        code_length = 1
        while code_length < 64:
            TEMP00 = input1[now:now+16]
            zero_and_length = AC_check(TEMP00) 
            #print(TEMP00)
            #print(zero_and_length)
            if zero_and_length == 3:
                code_length = 64
                temp01.append('EOB')
                now += 4
            elif zero_and_length == 31:
                code_length += 16
                temp01.append([15,0])
                now += 11
            else:
                code_length += (iRLE_code[zero_and_length][0]) 
                now += len(iAC_Huff[zero_and_length])
                temp02 = input1[now:now+iRLE_code[zero_and_length][1]]
                code_length += 1
                now += len(temp02)
                temp02 = bin_to_int(temp02)
                temp02 = [iRLE_code[zero_and_length][0], temp02]
                temp01.append(temp02)
        out_list.append(temp01)
        
    return out_list, now


def InvHuff_CbCr_test(inp,h,w):   #整體運行
    piece_size = h*w
    now = 0
    input1 = inp
    out_list = []
    for i in range(piece_size):
        ##################DC
        TEMP00 = input1[now:now+9]
        temp01 = []
        diff_length = DC_check(TEMP00)
        now += len(DC_Huff[diff_length])
        if diff_length == 0:
            temp01.append(0)
        else:
            temp02 = input1[now:now+diff_length]
            now += len(temp02)
            temp02 = bin_to_int(temp02)
            temp01.append(temp02)
        #print(now- tttt)
        ####################AC
        code_length = 1
        while code_length < 64:
            TEMP00 = input1[now:now+16]
            zero_and_length = AC_CbCr_check(TEMP00) 
            #print(TEMP00)
            #print(zero_and_length)
            if zero_and_length == 3:
                code_length = 64
                temp01.append('EOB')
                now += 4
            elif zero_and_length == 31:
                code_length += 16
                temp01.append([15,0])
                now += 11
            else:
                code_length += (iRLE_code[zero_and_length][0]) 
                now += len(iAC_Huff[zero_and_length])
                temp02 = input1[now:now+iRLE_code[zero_and_length][1]]
                code_length += 1
                now += len(temp02)
                temp02 = bin_to_int(temp02)
                temp02 = [iRLE_code[zero_and_length][0], temp02]
                temp01.append(temp02)

                #AC_cbcr[]

        out_list.append(temp01)
        
    return out_list, now