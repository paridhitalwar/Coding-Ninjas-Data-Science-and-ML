# You are given a rope of length 5m. Cut the rope into 9 parts such that each part is of equal length.
# Note:Array elements are the points where cut is to be made and round upto 2 decimal place.
# Print the array element.

import numpy as np

a=np.linspace(0,5,10)[1:9]
a=list(a)

for i in a:
    i=round(i,2)
    print(i)
