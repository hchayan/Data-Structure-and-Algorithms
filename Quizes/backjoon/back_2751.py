import sys

n = int(sys.stdin.readline().rstrip())


ans = []
for i in range(n):
    ans.append(int(sys.stdin.readline().rstrip()))

for i in sorted(ans):
    print(i)
