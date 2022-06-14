#main
n = int(input())

binary = 0
power = 1

while n > 0 :
	lastBit = n % 2
	binary += (lastBit * power)
	power *= 10
	n = n // 2

print(binary)
