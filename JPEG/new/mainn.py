import numpy as np
import time
import Def2
import combine_main


rows=256
cols=256
channels =1
w = 32
i = 0
t = 16

img=np.fromfile(r'lena', dtype='uint8')
img=img.reshape(rows, cols, channels)
start = time.time()
abc = Def2.encode(img, w)
#abc = combine_main.encode(img)
#print(abc)

#bcd = Def2.decode(abc, w)
#bcd = combine_main.decode(abc)
#print(bcd)
end = time.time()
print(format(end-start))