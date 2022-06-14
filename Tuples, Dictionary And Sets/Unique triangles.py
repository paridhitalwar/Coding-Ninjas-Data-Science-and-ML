n=int(input())
l1=[]
l2=[]
ct=0
for i in range(0,n):
    l1=list([i.strip() for i in input().split(' ')])
    l2.append(l1)
for i in range(0,len(l2)):
    l2[i].sort()
    l2[i]=int("".join(l2[i]))

 
l3=list(set(l2))
for i in range(0,len(l3)):
    if l2.count(l3[i])==1:
        ct=ct+1
print(ct)
