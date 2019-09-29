import sys

n = int(sys.stdin.readline().rstrip())

lis = [0]*(n+1)

for x in range(2, n+1):
    lis[x] = lis[x - 1] + 1
    if x%3==0:
        lis[x] = min(lis[x],lis[x//3]+1)
    if x%2==0:
        lis[x] = min(lis[x],lis[x//2]+1)

print(lis[n])