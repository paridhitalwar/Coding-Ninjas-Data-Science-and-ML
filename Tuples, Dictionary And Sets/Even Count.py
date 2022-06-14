def evenCount(arr):
    map1 = {}
    for i in range(0,n):
        if arr[i] not in map1:
            map1[arr[i]] = False
        else:
            map1[arr[i]] = not map1[arr[i]]
            
    for j in range(0,n):
        if map1[arr[j]] == True:
            break
    return arr[j]

# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
print(evenCount(arr))
