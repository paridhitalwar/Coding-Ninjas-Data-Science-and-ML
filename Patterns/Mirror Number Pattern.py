num=int(input())
i=1
while i<=num:
    spaces=1
    while spaces <=num-i:
        print(" ",end="")
        spaces=spaces+1
    stars=1
    while stars<=i:
        print(stars,end="")
        stars=stars+1
    print()
    i=i+1
