N = int(input())
# To parse through the whole string.
#remember to keep initialization such as even and odd here outside the loop.
even = 0
odd = 0
while(N > 0):
    rem = N % 10
    N = N // 10
    if (rem % 2 == 0):
        even = even + rem
    else:
        odd = odd + rem    
print(even," ", odd)
