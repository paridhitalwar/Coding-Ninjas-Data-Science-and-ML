#main
num = int(input())

decimal = 0
power = 1

while num > 0 :
	last = num % 10
	decimal += last * power
	power *= 2
	num = num // 10

print(decimal)
