from sys import stdin


def reverseEachWord(string):
    arr = string.split(' ')
    ans = ''
    for i in range(len(arr)):
        temp = arr[i]
        temp = temp[::-1]
        ans += temp + ' '
    return ans
