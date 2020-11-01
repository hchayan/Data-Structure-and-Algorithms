# 1,2자리수 수는 전부 한수..

import sys

n = int(sys.stdin.readline().rstrip())

def han(n):
    if n==1000: n-=1
    ans = 0
    for i in range(100, n+1):
        if (i%100)//10*2 == i%10 + i//100:
            ans+=1
    return ans


if n < 100 and n > 0:
    print(n)
else:
    print(99+han(n))




