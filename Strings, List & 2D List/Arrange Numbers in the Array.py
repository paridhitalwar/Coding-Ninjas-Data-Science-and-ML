from sys import stdin

def arrange(arr, n) :
    left = 0
    right = n - 1
    counter = 1
        
    while left <= right :
            
        if counter % 2 == 1 :
            arr[left] = counter
            counter += 1
            left += 1
        else :
            arr[right] = counter
            counter += 1
            right -= 1



