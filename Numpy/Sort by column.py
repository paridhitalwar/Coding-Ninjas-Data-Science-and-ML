import numpy as np

arr2D = np.array ([[21,20, 19, 18, 17],[16, 15, 14, 13, 12],[11, 10,  9,  8,  7],[ 6,  5,  4,  3,  2]])

# Sort 2D numpy array by 2nd Column
sortedArr = arr2D[arr2D[:,1].argsort()]
 
print(sortedArr)
