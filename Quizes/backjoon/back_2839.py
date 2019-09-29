import sys

x = int(sys.stdin.readline().rstrip())
ans = x                                                     # 초기 ans값 : 입력값(결과로 나올수 없는 큰값)

for i in range(x//3+1):                               # 3kg짜리만 있을때 제일 개수 많을때니 이를 범위로 설정
	a = i                                                     # a : 3kg개수
	b = (x - a*3)//5                                      # b : 5kg개수
	
	if (x-a*3)%5 == 0:                                  # b의 개수가 정수일때
		if ans > a+b:                                     # 결과값이 a+b보다 클때
			ans = a+b
			
print(ans) if ans != x else print(-1)             # ans값이 초기 ans값과 같으면 정답이 없는거니 -1출력
		