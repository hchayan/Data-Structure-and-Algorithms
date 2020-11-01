import sys

n = int(sys.stdin.readline().rstrip())

t1 = sorted(list(map(int,sys.stdin.readline().rstrip().split())))
t2 = sorted(list(map(int,sys.stdin.readline().rstrip().split())), reverse=True)

ans = 0
for i in range(n):
    ans += t1[i]*t2[i]

print(ans)