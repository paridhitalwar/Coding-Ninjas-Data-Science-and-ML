import numpy as np
input_=np.arange(1,21,1)
input_=input_.reshape(4,5)

x = input_[2:3,0:3]
for i in range(len(x)):
    print(*x[i],end=" ")

print()
    
y = input_[1:4,3:4]
for i in range(len(y)):
    print(*y[i],end=" ")
    
print()

z = input_[2:4]
for i in range(len(z)):
    print(*z[i],end=" ")
    
print()

w = input_[1:3,1:3]
for i in range(len(w)):
    print(*w[i],end=" ")
