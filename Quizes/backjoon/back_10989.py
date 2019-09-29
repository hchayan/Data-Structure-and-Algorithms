import sys

ans = [0]*10001
for i in range(int(sys.stdin.readline())):
    ans[int(sys.stdin.readline())] += 1


for i in range(10001):
    if ans[i] != 0:
        for j in range(ans[i]):
            print(i)