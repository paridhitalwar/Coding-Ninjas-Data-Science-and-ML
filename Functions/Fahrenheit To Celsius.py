def printTable(start,end,step):
    currentValue = start
    while(currentValue <= end):
        fValue = int((5/9)*(currentValue-32))
        print(currentValue,end="\t")
        print(fValue)
        currentValue = currentValue + step
s = int(input())
e = int(input())
step = int(input())
printTable(s,e,step)
