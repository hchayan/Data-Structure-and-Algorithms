


import sys

ans = []
maxx = 0
for i in range(5):
    x = sum(map(int, sys.stdin.readline().rstrip().split(" ")))
    ans.append(x)
    if x > maxx:
        maxx = x

print(ans.index(maxx)+1, maxx)