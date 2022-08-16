DC_Huff = ['00', '010', '011', '100', '101', '110', '1110', '11110', '111110', '1111110', '11111110', '111111110' ]

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
def invRLE_code(a):
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
    return iRLE_code[a]

def bin_to_int(list1):
    if list1[0] != '0':
        list1 = int(list1, 2)
    else:
        list1 = ''.join('1' if x == '0' else '0' for x in list1)
        list1 = int(list1, 2)
        list1 *= -1
    return list1

def InvHuff(inp):
    input = inp
    temp8 = []
    z = 0

    temp6 = []
    ############DC##############
    a=0
    b=0
    c=z+1
    temp = []
    temp3 = []
    temp.append(input[z])
    temp2 =''.join(temp)
    while temp2 != DC_Huff[a]:
        if temp2[b] == DC_Huff[a][b]:
            temp.append(input[c])
            c+=1
            b+=1
        else:
            a+=1
        temp2 =''.join(temp)
        
    for j in range(a):
        temp3.append(input[c+j])
    output0 = temp3
    output1 =''.join(output0)
    output1 = bin_to_int(output1)
    temp6.append(output1)
    ##########AC############
    temp4 = []
    temp7 = []
    temp5 = ''
    output4 = []
    print(j)
    d = c+j+1
    e = 0
    f = 0
    while temp6[len(temp6)-1] != 'EOB':
        temp4.append(input[d])
        temp5 =''.join(temp4)
        while temp5 != iAC_Huff[e]:
            print(temp4)
            print(iAC_Huff[e])
            if temp5[f] == iAC_Huff[e][f]:
                temp4.append(input[d+1])
                d+=1
                f+=1
            else:
                e+=1
            temp5 =''.join(temp4)
        output4 = invRLE_code(e)
        for l in range(output4[1]):
            temp7.append(input[d+l+1])
        d += (output4[1]+1)
        output2 = temp7
        output3 =''.join(output2)
        
        if output4 == invRLE_code(3):
            temp6.append('EOB')
        else:
            output3 = bin_to_int(output3)
            output4[1] = output3
            temp6.append(output4)
        temp4 = []
        temp7 = []
        temp5 = ''
        output4 = []
        e = 0
        f = 0
    z = d
    temp8.append(temp6)
    return temp8

print(InvHuff('1000001010'))
#'100 000  11011 10  01 01  00 0  01 00  00 1 11011 01 01 10 1100 0 00 0 1111011 1 00 0 11100 1 1010'
#[-7, [1, 2], [0,-2], [0, -1], [0, -3], [0, 1], [1, -2], [0, 2], [1, -1], [0, -1], [6 ,1], [0, -1], [2, 1], 'EOB']