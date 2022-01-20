def reverse(n):
    rev = 0
    while(n > 0):
        reminder = n % 10
        rev = (rev * 10) + reminder
        n = n // 10
    return rev 


n=int(input())
result = reverse(n)
print(result)
