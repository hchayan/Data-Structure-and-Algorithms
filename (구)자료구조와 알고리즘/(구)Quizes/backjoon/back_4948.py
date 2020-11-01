
def sosu(n):
    if n<1:
        return 0
    if n==1:
        return 1
    lis = [False, False] + [True]*(2*n-1)

    for i in range(2, int(2*n**.5)+1):
        if lis[i]:
            for a in range(i*2, 2*n+1, i):
                lis[a] = False
    return lis[n+1:].count(True)

import sys
x = int(sys.stdin.readline().rstrip())
while x!=0:
    print(sosu(x))
    x = int(sys.stdin.readline().rstrip())

