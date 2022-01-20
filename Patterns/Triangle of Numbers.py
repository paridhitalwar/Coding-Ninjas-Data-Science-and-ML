n =  int(input())
i = 1
while (i <= n):
    spaces =1
    while (spaces <= n-i):
        print(" ", end='')
        spaces += 1
    
    j = 1
    p = i
    while (j <= i):
        print(p, end='')
        p +=1
        j +=1 
    
    k = 1
    p = 2*i-2
    while (k <= i-1):
        print(p, end='')
        k +=1
        p -=1
    print()
    i +=1
