# 백준 알고리즘 4673번 문제


def d(n):                              # 숫자 n의 생성자를 구하는 함수(for문 안쓰고 일일히 나누기 1000, 100, 10, 1일때 값 구해서 더해줘도 됨)
	total = n
	for j in str(n):
		total += int(j)
	return total
	
lis = [True]*10000



'''
for i in range(1,len(lis)+1):    # 여기서 잘못 생각한게 for문을통해 1~10000내의 값들의 생성자 다 확인할수 있는데 밑에 while문써서 생성자의 생성자들 값을 또 확인함
	temp = d(i)
	while temp < len(lis)+1:
		lis[temp-1] = False
		temp = d(temp)
'''	
            

			
for i in range(1, len(lis)+1):   # 이 형태로만 했어도 충분히 범위내 값 다 검색 가능!
	if d(i) < 10001:
		lis[d(i)-1] = False

		
		
for k in range(len(lis)):        # 리스트 내 값이 True면 출력
	if lis[k]:               
		print(k+1)
		