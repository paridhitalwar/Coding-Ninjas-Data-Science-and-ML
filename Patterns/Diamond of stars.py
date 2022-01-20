n = int(input())
# top half
n1 = (n+1)//2

i = 1
while i <= n1:
    j = 1
    #top spaces
    while j <= n1 - i:
        print(' ', end = '')
        j +=1
    
    #top stars
    k = 1
    while k <= 2 * i - 1:
        print('*',end = '')
        k +=1   
    i +=1
    print()

n2 = n//2
y = 1
while y <= n2:

    #bottom spaces
    l = 1
    while l <= y:
        print(' ',end = '')
        l +=1
        
    #bottom star
    m = 1
    while m <= n1+n2-2 * y :
        print('*',end = '')
        m +=1
    
    y +=1
    print()
