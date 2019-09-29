import sys

c, n = list(map(int,sys.stdin.readline().rstrip().split()))
x = list(map(int,sys.stdin.readline().rstrip().split()))

ans = 0
for i in range(c-2):
    for j in range(i+1,c-1):
        for k in range(j+1, c):
            print(i,j,k)
            if x[i]+x[j]+x[k] > ans and x[i]+x[j]+x[k] <= n:
                ans = x[i]+x[j]+x[k]
print(ans)

