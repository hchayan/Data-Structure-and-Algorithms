import math

print(math.floor(math.sqrt(10)))


num = 10

def sosu(num):
	for i in range(2,num+1):
		if (num)%i != 0:
			print(i)

sosu(num)