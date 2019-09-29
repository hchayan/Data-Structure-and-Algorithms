'''
분수들을 순서대로 나열해보면

1/1 -> 1/2 -> 2/1 -> 3/1-> 2/2 -> 1/3 -> 1/4 -> 2/3 -> 3/2 -> 4/1 ...

순으로 늘어난다.

이때 분자와 분모를 따로따로 나누어 보면

1 / 1 2 / 3 2 1 /1 2 3 4 ...
1 / 2 1 / 1 2 3 /4 3 2 1...

순으로 증가함을 볼수 있고 이를

'''
import sys

x = int(sys.stdin.readline().rstrip())

temp_x = x                                                # temp_x : 원본x 손상되지 않고 계산용으로 사용하기 위한 변수            
home = 1                                                  # home-1 : 숫자의 번지수
sum = 0
while temp_x > 0:                                      # 입력한 숫자의 번지수 찾는 while문
	temp_x -= home
	sum += home
	home +=1

bunmo = 0
bunza = 0

if (home-1) % 2 == 0:                                  # 번지수가 짝수면
	bunza = home-1 - (sum - x)
	
else:
	bunza = (sum-x)+1
bunmo = home - bunza

print(str(bunza)+"/"+str(bunmo))
	