# O(n)

import sys

x = int(sys.stdin.readline().rstrip())

lis = list(map(int, sys.stdin.readline().rstrip().split(" ")))
now, ans = 0, 0
for i in range(1,x):
    if lis[i-1] < lis[i]:
        now += (lis[i]-lis[i-1])
    else:
        now = 0
    if now > ans:
        ans = now

print(ans)

