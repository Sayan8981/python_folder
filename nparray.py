
import numpy as np
import time

#array_list = np.array([])
array_list = []
print (array_list)


for i in range (0, 1000000):
    #import pdb;pdb.set_trace()
    print(i)
    array_list = np.insert(array_list, i, i, axis=None)
    print (array_list)
    print (time.ctime())
        