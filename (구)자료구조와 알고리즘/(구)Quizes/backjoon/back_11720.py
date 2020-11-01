import sys

n = int(sys.stdin.readline().rstrip())

x = sys.stdin.readline().rstrip()
ans = 0

for i in range(n):
	ans += int(x[i])
	
print(ans)
	
	