import numpy as np

b = np.zeros(10,dtype = int)
b[4] = 1

for x in range(len(b)):
    print(b[x],end=" ")
