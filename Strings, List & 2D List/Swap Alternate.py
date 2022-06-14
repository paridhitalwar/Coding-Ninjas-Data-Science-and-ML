from sys import stdin

def swapAlternate(arr, n) :
    for i in range(0, (n-1), 2):
        temp = arr[i]
        arr[i] = arr[i+1]
        arr[i+1] = temp
    return arr
