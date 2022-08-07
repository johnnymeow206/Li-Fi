import numpy as np
from sympy import pi
import cv2
import Def
import FDCT
import FDCT_more
import time

m =np.array([[36, 20, 24, 58, 18, 9, 8, 7],
            [117, 86, 53, 67, 29, 9, 5, 6],
            [46, 75, 103, 141, 124, 81, 28, 15],
            [15, 14, 17, 50, 42, 82, 85, 68],
            [12, 13, 8, 7, 7, 26, 99, 111],
            [12, 10, 9, 11, 38, 110, 130, 83],
            [9, 11, 13, 53, 118, 117, 89, 83],
            [7, 14, 68, 128, 113, 85, 90, 140]])

m = m.astype(np.float32)
print(m)
m -= 128*np.ones((8,8))
Fm = FDCT_more.FDCT3(m)
print(Fm)
Qm = Def.quan(Fm)
#Qm = np.round_(Qm,1)
Qm = np.round_(Qm,0)
print(Qm)
iQm = Def.iquan(Qm)
print(iQm)
#iQm = iQm.astype(np.float32)
fm = FDCT_more.iFDCT3(iQm)
fm += 128*np.ones((8,8))

#fm = abs(fm)
print(fm)

