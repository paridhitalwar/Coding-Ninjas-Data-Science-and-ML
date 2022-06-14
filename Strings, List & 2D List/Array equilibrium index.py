from sys import stdin

def arrange(arr, n) :
    #Your code goes here
    for i in range(n):
        if arr[i]%2!=0:
            print(arr[i],end=" ")
            
    for j in reversed(range(n)) :
        if arr[j]%2==0:
            print(arr[j],end=" ")


#to print the array/list
def printList(arr, n) :
    for i in range(n) :
        print(arr[i], end = ' ')
    print()



#main
t = int(stdin.readline().strip())

while t > 0 :
    n = int(stdin.readline().strip())
    arr = n * [0]
    arrange(arr, n)
    printList(arr, n)
    t -= 1
