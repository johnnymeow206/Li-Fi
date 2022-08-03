import numpy as np
import math
import time
'''
start = time.time()

a = np.ones((1,64))*127
f = np.ones((8,8))
F = np.ones((8,8))
for u in range(8):
    for  v in range(8):
        if u == 0 and v == 0:
            cucv = 1/2
        else:
            cucv = 1
        Cx = np.asmatrix(np.array([math.cos(((2*x+1)*u*math.pi)/16) for x in range (8)]))
        Cy = np.asmatrix(np.array([math.cos(((2*y+1)*v*math.pi)/16) for y in range (8)]))
        C = np.reshape(np.transpose(Cx)*Cy,(64,1))
        F[u,v] = 0.25*cucv*a*C
print(F)
F = np.reshape(F,(1,64))
F[0,0]=F[0,0]*0.5
for x in range(8):
    for  y in range(8):
        Cx = np.asmatrix(np.array([math.cos(((2*x+1)*u*math.pi)/16) for u in range (8)]))
        Cy = np.asmatrix(np.array([math.cos(((2*y+1)*v*math.pi)/16) for v in range (8)]))
        print(cucv)
        C = np.reshape(np.transpose(Cx)*Cy,(64,1))
        f[x,y] = 0.25*cucv*F*C
print(f)
end = time.time()
print(format(end-start))
'''
def FDCT3(S):
    F = np.ones((8,8))
    M = []
    m0 = np.array([1/(2*math.sqrt(2)) for x in range (8)])
    m1 = [[0 for k1 in range(8)] for k2 in range(7)]
    for u0 in range(7):
        u = u0+1
        m1[u0] = np.array([0.5*math.cos(((2*v+1)*u*math.pi)/16) for v in range (8)])
    M = np.asmatrix(np.vstack((m0,m1)))
    F = M*S*np.transpose(M)
    return F
def iFDCT3(S1):
    f = np.ones((8,8))
    M = []
    m0 = np.array([1/(2*math.sqrt(2)) for x in range (8)])
    m1 = [[0 for k1 in range(8)] for k2 in range(7)]
    for u0 in range(7):
        u = u0+1
        m1[u0] = np.array([0.5*math.cos(((2*v+1)*u*math.pi)/16) for v in range (8)])
    M = np.asmatrix(np.vstack((m0,m1)))
    f = np.transpose(M)*S1*M
    return f

#m1 = np.vstack(np.array([0.5*math.cos(((2*v+1)*u*math.pi)/16) for v in range (8)]))