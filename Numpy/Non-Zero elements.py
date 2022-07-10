import numpy as np

a = np.array([1,2,0,0,4,0])

ind1 = np.where(a != 0)

for i in ind1:
    print(*i,end= " ")
