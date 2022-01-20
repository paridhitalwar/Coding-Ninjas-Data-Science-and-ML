n = int(input())
i = 1
while i <= n :
    j = 1
    start_char = chr(ord('A') + n -1)
     
    while j <= i:
        charP = chr(ord(start_char)-i +j)
        print(charP, end = '')
        j += 1
    print()
    i += 1
