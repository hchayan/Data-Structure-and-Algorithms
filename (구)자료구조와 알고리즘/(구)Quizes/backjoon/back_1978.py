# 백준 알고리즘 1978번

import sys

n = int(sys.stdin.readline().rstrip())              # sys문이 input문보다 훨씬 시간을 절약한다.

x_list = sys.stdin.readline().rstrip().split(" ")


def isPrime(x):                                             # 숫자 x가 소수인지 검사하는 함수
	if x < 2:
		return False
	for i in range(2, x):
		if x%i ==0:
			return False
	return True


ans = 0
for i in range(n):                                            # 입력한 수중에 소수가 있으면 ans 값 + 1을 한다.
	if isPrime(int(x_list[i])):
		ans+=1
		
print(ans)
		