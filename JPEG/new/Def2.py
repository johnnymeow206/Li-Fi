import Huff_try
DC_Huff = ['00', '010', '011', '100', '101', '110', '1110', '11110', '111110', '1111110', '11111110', '111111110' ]

AC_Huff = [['00','01' ,'100', '1011', '11010', '1111000', '11111000', '1111110110', '1111111110000010', '1111111110000011'],
           ['1100', '11011', '1111001', '111110110', '1111110110', '1111111110000100', '1111111110000101', '1111111110000110', '1111111110000111', '1111111110001000'],
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
           ['1111111111110101', '1111111111110110', '1111111111110111', '1111111111111000', '1111111111111001', '1111111111111010', '1111111111111011', '1111111111111100', '1111111111111101', '1111111111111110','11111111001','1010']]

           #0/0(EOF) 方便起見已移至最後一項
           #F/0 已移至倒數第二項

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
    diff = int_to_bin(diff)
    if diff == 0:
        temp[0] =  DC_Huff[0] + diff
    else:
        temp[0] =  DC_Huff[len(diff)] + diff
    i = 1
    ff00 = 1
    while ff00 != 64:
        if temp[i][0] == 'Z':     #ZRL detect
            temp[i] = '11111111001'
            ff00 += 16
            i += 1
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
'''
k = [-1, 'EOB']
print(Huff(k))
'''

def DC_check(inp1):
    list001 = inp1
    for ff01 in range(12):
        list002 = list001[0:len(DC_Huff[ff01])]
        if list002 == DC_Huff[ff01]:
            return ff01     #DC的長度
    
def AC_check(inp1):
    list001 = inp1
    list002 = list001[0:4]
    list003 = list001[0:11]
    if list002 == "1010":           #先檢查EOB
        return 'EOB'
    elif list003 == "11111111001":  #再檢查ZRL
        return 'ZRL'
    else:
        for ff01 in range(16):      #0~F(16)前面有幾個零
            for ff02 in range(10):  #1~A(10)後面有幾位數(不可能為零)
                list002 = list001[0:len(AC_Huff[ff01][ff02])]
                if list002 == AC_Huff[ff01][ff02]:
                    return [ff01, ff02+1]       #回傳幾個零,後有幾位數

def InvHuff(inp):   #整體運行
    w = 32
    now = 0
    input1 = inp
    out_list = []
    for i in range(1024):
        #for j in range(w):
            temp01 = []
            ##################DC
            TEMP00 = input1[now:now+9]
            diff_length = DC_check(TEMP00)
            now += len(DC_Huff[diff_length])
            temp02 = input1[now:now+diff_length]
            now += len(temp02)
            temp02 = bin_to_int(temp02)
            temp01.append(temp02)
            ####################AC
            code_length = 1
            while code_length < 64:
                TEMP00 = input1[now:now+16]
                zero_and_length = AC_check(TEMP00) 
                
                if zero_and_length == 'EOB':
                    code_length = 64
                    temp01.append(zero_and_length)
                    now += 4
                elif zero_and_length == 'ZRL':
                    code_length += 16
                    temp01.append([15,0])
                    now += 11
                else:
                    code_length += (zero_and_length[0]+1)
                    now += len(AC_Huff[zero_and_length[0]][zero_and_length[1]-1])
                    temp02 = input1[now:now+zero_and_length[1]]
                    now += len(temp02)
                    temp02 = bin_to_int(temp02)
                    temp02 = [zero_and_length[0], temp02]
                    temp01.append(temp02)
            out_list.append(temp01)
            
    return out_list
