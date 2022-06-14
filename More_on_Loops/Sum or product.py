num=int(input())
c=int(input())

if c==1:
    res=0
    for i in range(1,num+1):
        res=res+num
        num=num-1
    print(res)
elif c==2:
    res=1
    for i in range(1,num+1):
        res=res*num
        num=num-1
    print(res)
else:
    print(-1)
