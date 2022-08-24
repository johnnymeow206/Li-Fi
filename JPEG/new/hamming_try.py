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
        p0 += 1
        p2 += 1
    if m1[0][2] == '1':
        p1 += 1
        p2 += 1
    if m1[0][3] == '1':
        p0 += 1
        p1 += 1
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
print(m2)
#  !!要補個偵測最後少於四個的標誌能讓decoder知道!!
###############decoder#################
hamming_743code = ['0000000','0001111','0010011','0011100','0100101','0101010','0110110','0111001',
                   '1000110','1001001','1010101','1011010','1100011','1101100','1110000','1111111']
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




