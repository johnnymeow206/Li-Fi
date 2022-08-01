import numpy as np
import math
import time

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