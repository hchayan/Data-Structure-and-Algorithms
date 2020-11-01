import sys

n, k = list(map(int,sys.stdin.readline().rstrip().split()))

tmp1 = 1
tmp2 = 1
for i in range(k):
    tmp1 *= (n-i)
    tmp2 *= (i+1)

print((tmp1//tmp2)%10007)