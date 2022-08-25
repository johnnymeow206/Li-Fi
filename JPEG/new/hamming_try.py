##############encoder################
p0 = p1 = p2 = 0
d = 0
m2 = []
m = ['00110111']
len_of_m = len(m[0])
len_of_m1 = 0
while len_of_m != len_of_m1:
    m1 = [m[0][0+d:4+d]]
    len_of_m1 += len(m1[0])
    if len(m1[0]) != 4:
        for b in range(4-len(m1[0])):
            m1.append('0')
        m1 = [''.join(m1)]
    if m1[0][0] == '1':
        p0 += 1
        p1 += 1
    if m1[0][1] == '1':
        p1 += 1
        p2 += 1
    if m1[0][2] == '1':
        p0 += 1
        p1 += 1
        p2 += 1
    if m1[0][3] == '1':
        p0 += 1
        p2 += 1

    p0_num_one = p0 % 2
    p1_num_one = p1 % 2
    p2_num_one = p2 % 2

    if p0_num_one == 0:
        m1.append('0')
    else:
        m1.append('1')
    if p1_num_one == 0:
        m1.append('0')
    else:
        m1.append('1')
    if p2_num_one == 0:
        m1.append('0')
    else:
        m1.append('1')

    m1 = ''.join(m1)
    m2.append(m1)
    p0 = p1 = p2 = 0
    d += 4
m2 = ''.join(m2)
#print(m2)
#  !!要補個偵測最後少於四個的標誌能讓decoder知道!!
###############decoder#################
hamming_743code = ['0000000','0001101','0010111','0011010','0100011','0101110','0110100','0111001',
                   '1000110','1001011','1010001','1011100','1100101','1101000','1110010','1111111']
def hamming_check(inp1):
    list001 = inp1
    for ff01 in range(16):
        if list001 == hamming_743code[ff01]:
            return list001[0:4]    #取前四個
def code_change(inp, i):
    temp = list(inp)
    if temp[i] == '0':
        temp[i] = temp[i].replace('0', '1')
    else:
        temp[i] = temp[i].replace('1', '0')
    temp = ''.join(temp)
    return temp
def errorcheck(inp):
    temp = inp
    synd_code0 = int(temp[4]) + int(temp[0]) + int(temp[2]) + int(temp[3])
    synd_code1 = int(temp[5]) + int(temp[0]) + int(temp[1]) + int(temp[2])
    synd_code2 = int(temp[6]) + int(temp[1]) + int(temp[2]) + int(temp[3])
    synd_code0 = synd_code0 % 2
    synd_code1 = synd_code1 % 2
    synd_code2 = synd_code2 % 2
    if  synd_code0 == 0 and synd_code1 == 0 and synd_code2 == 0:#沒有錯
        temp = temp
    elif synd_code0 == 1 and synd_code1 == 1 and synd_code2 == 0:#第1個錯
        temp = code_change(temp, 0)
    elif synd_code0 == 0 and synd_code1 == 1 and synd_code2 == 1:#第2個錯
        temp = code_change(temp, 1)
    elif synd_code0 == 1 and synd_code1 == 1 and synd_code2 == 1:#第3個錯
        temp = code_change(temp, 2)
    elif synd_code0 == 1 and synd_code1 == 0 and synd_code2 == 1:#第4個錯
        temp = code_change(temp, 3)
    elif synd_code0 == 1 and synd_code1 == 0 and synd_code2 == 0:#第5個錯
        temp = code_change(temp, 4)
    elif synd_code0 == 0 and synd_code1 == 1 and synd_code2 == 0:#第6個錯
        temp = code_change(temp, 5)
    elif synd_code0 == 0 and synd_code1 == 0 and synd_code2 == 1:#第7個錯
        temp = code_change(temp, 6)
    return temp
'''
m3 = '1011010'
#TEMP00 = code_change(m3, 0)
TEMP00 = errorcheck(m3)
print(TEMP00)
'''
m3 = '10110100111001'#假設第一位錯
decode_m1 = m3
decode_m2 = ['']
now = 0
len_m2 = 0.
block_decode_m1 = len(decode_m1)/7
block_decode_m2 = len_m2/4
while block_decode_m1 != block_decode_m2:
    TEMP00 = decode_m1[now:now+7]
    TEMP00 = errorcheck(TEMP00)
    decode_m2.append(hamming_check(TEMP00))
    decode_m2 = [''.join(decode_m2)]
    len_m2 = len(decode_m2[0])
    block_decode_m2 = len_m2/4
    now += 7
print(decode_m2)
'''
de_m = m2
block_de_m = len(de_m)/7
temp_m = []
temp_m2 = ''
spot_m = 0
temp_m.append(de_m[spot_m])
temp_m2 = ''.join(temp_m)
de_m1 = []
block_de_m1 = len(de_m1)/4
i = 0
j = 0
while block_de_m != block_de_m1:
    while temp_m2 != hamming_743code[i]:
        if temp_m2[j] == hamming_743code[i][j]:
            spot_m += 1
            temp_m.append(de_m[spot_m])
            j += 1
            temp_m2 = ''.join(temp_m)
        else:
            i += 1
            j = 0
            spot_m = 0
            temp_m.append(de_m[spot_m])
            temp_m2 = ''
        
        print('j=', j )
        print(temp_m)
        print(temp_m2)
    temp_m1 = temp_m[0][0:4]
    de_m1.append(temp_m1)
    de_m1 = [''.join(de_m1)]
    print(de_m1)




'''




