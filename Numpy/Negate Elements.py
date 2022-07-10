import numpy as np

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

a[2:8] = np.multiply(a[2:8],-1)

for i in a:
    print(i)
