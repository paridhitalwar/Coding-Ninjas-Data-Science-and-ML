def maxFreq(l):
    d={}
    count , i = 0,''
    for item in reversed(l):
        d[item] = d.get(item , 0) + 1
        if d[item] >= count:
            count,i = d[item] ,item
    return(i)


# Main
n=int(input())
l=list(int(i) for i in input().strip().split(' '))
print(maxFreq(l))
