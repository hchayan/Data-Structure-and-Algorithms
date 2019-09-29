# 스택

import sys

n = int(sys.stdin.readline().rstrip())

ans = []
for i in range(n):
	x = int(sys.stdin.readline().rstrip())
	
	ans.pop() if x == 0 else ans.append(int(x))		
	
print(sum(ans))