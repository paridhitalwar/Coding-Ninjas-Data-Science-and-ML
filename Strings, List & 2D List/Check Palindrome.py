'''

    Time complexity: O(N)
    Space complexity: O(1)

    where N is the length of the input string

'''

from sys import stdin


def isPalindrome(string) :

    left = 0
    right = len(string) - 1

    while left < right :
        if string[left] != string[right] :
            return False

        left += 1
        right -= 1

    return True



#main
string = stdin.readline().strip();
ans = isPalindrome(string)

if ans :
    print('true')
else :
    print('false')

    
    
    
    
/* OR */



c=input()
if c[::-1] == c:
    print("true")
else:print("false")
