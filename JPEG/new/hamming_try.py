
'''
m1 = m2 = m3 = m4 = 0
p0 = m1 + m2 + m4
p1 = m1 + m3 + m4
p2 = m2 + m3 + m4
'''
p0 = p1 = p2 = 0
d = 0
m2 = []
m = ['0011010']
for a in range(2):
    m1 = [m[0][0+d:4+d]]
    if len(m1[0]) != 4:
        print(len(m1))
        for b in range(3-len(m1)):
            m1.append('0')
        m1 = ''.join(m1)
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
