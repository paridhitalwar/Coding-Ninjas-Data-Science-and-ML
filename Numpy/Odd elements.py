import numpy as np

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

ind1 = np.where(a % 2 == 1)

for i in ind1:
    a[i] = -1
    print(*a)
