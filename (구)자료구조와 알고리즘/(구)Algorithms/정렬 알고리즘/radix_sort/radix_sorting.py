# 기수 알고리즘



def radix(list_to_order):
	is_sorted = False;
	position = 1;
	
	while not is_sorted:                                     # is_sorted 변수가 False일때 반복 실행
		is_sorted = True;
		
		queue_list = [list() for _ in range(10)]        # queue_list = [[], [], [], [], [], [], [], [], [], []]
		
		
		for num in list_to_order:  						#정렬해야할 list의 각 원소 num
			digit_number = int((num/position)%10)# 원소를 position(자리수)만큼 나누고 %10을 통해 해당 자리수의 값을 확인. 
			# ex) num=153, position=10 =>    153/10 = 15 -> 15%10 = 5   : position(자리수) 10의 값은 5이다.
		
			queue_list[digit_number].append(num) # digit_number(해당자리수)에 해당되는 큐 위치에 원소를 삽입.
			
			if is_sorted and digit_number > 0:        #list에서 원소들 값이 있으면 실행
				is_sorted = False
				
				
		index = 0
		
		for nums in queue_list:                             # 각 자리수에 맡게 들어간 값들을 순서대로 빼서 다시 list에 삽입.
			for num in nums:     
				list_to_order[index] = num
				index +=1
			
		position *= 10                                            # 자리수 변경(1의자리수 -> 10의자리수 -> ...)
		
		
x = [35,41,55,41,54,49]
radix(x)
print(x)
