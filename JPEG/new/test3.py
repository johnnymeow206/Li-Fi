from PIL import Image
import numpy as np
import cv2
from sympy import cos, pi

rows=256
cols=256
channels =1

img=np.fromfile(r'lena', dtype='uint8')
img=img.reshape(rows, cols, channels)


cv2.imshow('Infared image-640*512-8bit',img)
#  If it is uint16 Please convert to uint8. otherwise , There will be a problem with the display .
cv2.waitKey()
cv2.destroyAllWindows()


n = np.transpose(img) 
print(n)