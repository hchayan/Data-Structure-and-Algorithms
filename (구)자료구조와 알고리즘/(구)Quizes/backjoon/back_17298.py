import sys

n = int(sys.stdin.readline().rstrip())
x = sys.stdin.readline().rstrip().split()
ans = "-1"

for i in range(len(x)-1, -1, -1):
	if i != len(x)-1:
		for j in range(i+1, len(x)+1):
			if j == len(x):
				ans = "-1 " + ans
			elif x[i] < x[j]:
				ans = x[j] + " " + ans
				break
print(ans)









'''
ans = ''
for i in range(n-1):
	if x[i] > max(x[i+1:n]):
		ans = ans + '-1 '
	else:
		for j in range( i+1 , n ):
			if x[i] < x[j]:
				ans = ans + x[j]+' '
				break

print(ans+"-1")
'''