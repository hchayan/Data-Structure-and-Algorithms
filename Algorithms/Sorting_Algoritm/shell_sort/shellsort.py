# 쉘 정렬 알고리즘

def gap_insert_sort(x_list, start, gap):                   
	for target in range(start+gap,len(x_list), gap):    # 중요
		
		val = x_list[target]
		i = target
		
		while i > start:
			if x_list[i-gap] > val:
				x_list[i] = x_list[i-gap]
			else:
				break
			i -= gap
	
		x_list[i] = val
		

def shell_sort(x):
	k = len(x) // 2                                            # k = 간격(배열길이/2)
	while k > 0:
		for i in range(k):                                   # 각 부분 리스트들간 i번째 자리 값들 삽입 정렬
			gap_insert_sort(x,i,k) 
			# print(x)
		k = k//2
	
x = [5,2,8,6,1,9,3,7]
shell_sort(x)
print(x)

'''
k = 8/2 = 4
gap_insert_sort(x,0,4)  => 전체리스트의 0,4번째수 비교 (부분 리스트 0번째 원소들끼리 비교 정렬)
gap_insert_sort(x,1,4) => 전체리스트의 1,5번째수 비교(부분 리스트 1번째 원소들끼리 비교 정렬)
gap_insert_sort(x,2,4) => 부분 2번째
gap_insert_sort(x,3,4) => 부분 3번째

k = 4/2 = 2
gap_insert_sort(x,0,2) =>4개의 부분 리스트 0번째 원소들간 삽입 정렬
...
'''