# 해결법
# 처음에 0~9까지에 가능한 숫자의 개수인 [0,1,1,1,1,1,1,1,1,1,1] 를 초기값으로 지정 ( 0은 불가능)
# 그리고 n번째 값을 n-1, n+1의 값에 더해준다.
# 이때 n이 0, 9면 각각, 1, 8에만 값 더해준다.
# 이를 반복


import sys

ans = [0]+[1]*9

for n in range(1,int(sys.stdin.readline().rstrip())):
	tmp = [0]*10
	for i in range(10):
		if ans[i] > 0:
			if i ==9:
				tmp[8] = tmp[8]+ans[9]
			elif i == 0:
				tmp[1] = tmp[1] + ans[0]
				
			else:
			    tmp[i+1] = ans[i] + tmp[i+1]
			    tmp[i-1] = ans[i] + tmp[i-1]
		
			
	ans = tmp
print(sum(ans)%1000000000)
