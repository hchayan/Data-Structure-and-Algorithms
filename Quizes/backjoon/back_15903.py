num = input().split(" ")
lis = list(map(int,input().split(" ")))


for i in range(int(num[1])):
	temp1 = 1000001
    for k in lis:
		if temp1 >= k:
			temp2 = temp1
			temp1 = k

			
	lis.remove(temp1)
	lis.remove(temp2)
	
	temp = temp1+temp2
	lis.append(temp)
	lis.append(temp)
		
print(sum(list))
		

		
	