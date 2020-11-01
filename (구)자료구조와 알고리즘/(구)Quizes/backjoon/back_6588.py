def isitPrime(num):
	list=[]
	for i in range(3, num, 2):
		if num%i !=0:
			list.append(i)
	return list


while True:
	num =int(input())
	
	if num == 0:
		break
		
	else:
		print(isitPrime(num))
	

		
		