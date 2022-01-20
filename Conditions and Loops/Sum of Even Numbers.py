N=int(input())
i=1
sum=0
while i<=N:
    if(i%2==0):
        sum=sum+i
        i=i+1
    else:
        i=i+1
print(sum)
