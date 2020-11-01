# 재귀함수

import sys

def facto(x):
	if x < 1:
		return 1
	return x*facto(x-1)
		

x = int(sys.stdin.readline().rstrip())

print(facto(x))