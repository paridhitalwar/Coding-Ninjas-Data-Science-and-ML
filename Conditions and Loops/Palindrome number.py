def checkPalindrome(num):
    temp = num
    rev = 0
    while(num > 0):
        reminder = num % 10
        rev = (rev * 10) + reminder
        num = num // 10
        
    if (temp == rev):
        return True
    else:
        return False
#Implement Your Code Here

		
num = int(input())
isPalindrome = checkPalindrome(num)
if(isPalindrome):
	print('true')
else:
	print('false')
