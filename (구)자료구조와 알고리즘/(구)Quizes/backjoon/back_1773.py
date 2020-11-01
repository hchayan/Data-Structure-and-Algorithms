

import sys

n, time = map(int, sys.stdin.readline().rstrip().split(' '))

lis = [0]*time
for nn in range(n):
    x = int(sys.stdin.readline().rstrip())
    if lis[x-1] != 1:
        for i in range(x, time+1, x):
            lis[i-1] = 1

print(lis.count(1))
