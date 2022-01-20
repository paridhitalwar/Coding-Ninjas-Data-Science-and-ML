n=int(input())
i=1
while i<=n:
    s=1
    while s<=n-i:
        print(' ', end='')
        s=s+1
    stars=1
    while stars<=i:
        print('*', end='')
        stars=stars+1
    stars=i-1
    while stars>=1:
        print('*', end='')
        stars=stars-1
    print()
    i=i+1
