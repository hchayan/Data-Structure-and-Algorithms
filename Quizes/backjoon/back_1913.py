import sys

n = int(sys.stdin.readline().rstrip())
x = int(sys.stdin.readline().rstrip())

lis = [[0 for i in range(n)] for i in range(n)]                                                                        # 값을 넣을 모든원소 0인 2차원 배열 생성

	
dx = [0,1,0,-1]       #dx, dy : 다음 원소 위치(방향) 결정용 값들(중요) - 탐색 순서 :  [(1,0) : 오른쪽] -> [(0,1) : 아래] -> [(-1,0) : 왼쪽] -> [(0,-1) 위] ***
dy = [-1,0,1,0]

a,b=0,0                # 현재 배열내 위치값
i = n*n                # i : 현재 원소값
d = 0                   # dx,dy배열에서 현재 방향 선택 값

while i > 0:         # 원소가 0이될때까지
	lis[a][b] = i      # 위치 a,b에 i 삽입
	
	if a+dx[d] <0 or b+dy[d] <0 or a+dx[d] >= n or b+dy[d] >=n or lis[a+dx[d]][b+dy[d]] != 0:    #다음 위치값이 0보다 작거나 n보다 크거나, 이미 값이 들어있는 자리이면
		d = (d+1)%4  #방향 변경
	
	a = a+dx[d]       # 다음 위치 a,b와 원소값 i 변경
	b = b+dy[d]       
	i-=1


for i in range(n):                               # 출력
	print(" ".join(map(str,lis[i])))           # int원소 -> str -> str문장
	if x in lis[i]:                                   # 찾는 원소값 찾으면 실행
		r1,r2 = i+1, lis[i].index(x)+1
		
print(r1, r2)  # 찾던 원소값 출력