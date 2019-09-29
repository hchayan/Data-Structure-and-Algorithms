# 주요개념 : 배열
import sys

x = int(sys.stdin.readline().rstrip())

for i in range(x):
	ox = sys.stdin.readline().rstrip()
	ans = 0
	stack = 0
	for k in range(len(ox)):
		if ox[k] == "O":
			stack+=1
			
		else:
			stack = 0
			
		ans+=stack
	print(ans)
