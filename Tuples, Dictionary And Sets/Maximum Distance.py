from sys import stdin

def maximumDistance(arr):

    maxDist = 0

    for i in range(len(arr)):

        for j in range(i + 1, len(arr)):

            if arr[i] == arr[j]:
                maxDist = max(maxDist, j - i)

    return maxDist


# Main Code.

n = int(input())

if n == 0:
    print 0
    exit()

arr = list(map(int, stdin.readline().strip().split(' ')))

ans = maximumDistance(arr)

print(ans)
