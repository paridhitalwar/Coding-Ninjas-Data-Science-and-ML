
'''

    Time complexity: O(N)
    Space complexity: O(1)

    where N is the length of the input String

'''

from sys import stdin


def highestOccuringChar(string) :
    n = len(string)
    frequency = [0] * 256
    maxFrequency = 0

    for i in range(n) :
        frequency[ord(string[i])] += 1   
        maxFrequency = max(maxFrequency, frequency[ord(string[i])]);

    answer = '\0'

    for i in range(n) :
        if frequency[ord(string[i])] == maxFrequency :  
            answer = string[i]
            break

    return answer



#main
string = stdin.readline().strip();
ans = highestOccuringChar(string)

print(ans)
