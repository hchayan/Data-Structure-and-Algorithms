#병합 정렬 알고리즘

def merge_sort(list):
	if len(list) <= 1:                                  # 입력 받은 list가 애초에 원소가 1개 이하이면 그냥 반환
		return list
	
	mid = len(list)//2
	
	leftList = merge_sort(list[:mid])         # 재귀
	rightList = merge_sort(list[mid:])
	
	return merge(leftList, rightList)        
	
	
	

def merge(left, right):                             # 입력받은 두 리스트를 2차 병합 정렬방식으로 병합하는 함수
	res = []
	
	while len(left) > 0 or len(right) > 0:     # 새롭게 정렬 안된 원소가 없을때까지
	
		if len(left) > 0 and len(right) >0:      # 입력 받은 두 리스트 모두 아직 새롭게 정렬안된 원소가 있으면..(비교해 삽입)
			if left[0] < right[0]:
				res.append(left[0])
				left = left[1:]
			else:
				res.append(right[0])
				right = right[1:]
				
		elif len(left) > 0:
			res.append(left[0])
			left = left[1:]
			
		elif len(right) >0:
			res.append(right[0])
			right = right[1:]
			
	return res
	
	
x = [5,2,8,6,1,9,3,7]
print(merge_sort(x))
			
				