n=int(input())
i=1
while i<=n:
    start_char = chr(ord('A') + i -1)
    j=1
    while j<=i:
        print(start_char, end='')
        j=j+1
    print()
    i=i+1
