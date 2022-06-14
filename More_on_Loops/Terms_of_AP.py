n=int(input())
count=1
current=1

while(count<=n):
    num=3*current+2
    if num % 4 != 0:
        print(num, end=' ')
        count=count+1
    current=current+1
