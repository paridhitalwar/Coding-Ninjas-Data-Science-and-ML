from sys import stdin

def removeConsecutiveDuplicates(string) :
    n =  len(string)
    ans = ""
    startIndex = 0
    while startIndex <n:
        uniqueChar = string[startIndex]
        nextUniqueCharIndex = startIndex + 1
        
        while ((nextUniqueCharIndex <n) and (string[nextUniqueCharIndex]==uniqueChar)):
            nextUniqueCharIndex += 1
        
        ans += uniqueChar
        startIndex = nextUniqueCharIndex
    return ans
