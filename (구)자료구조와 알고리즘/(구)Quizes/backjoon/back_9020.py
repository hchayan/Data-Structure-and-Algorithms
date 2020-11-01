def isPrime(a):
    if a<2:
        return False

    for i in range(2,int(a**.5)+1):
        if a%i==0:
            return False
    return True

import sys
n = int(sys.stdin.readline().rstrip())
for nn in range(n):
    x = int(sys.stdin.readline().rstrip())

    #lis = [isPrime(i) for i in range(x)]

    for i in range(x//2, 0, -1):
        if isPrime(i) and isPrime(x-i):
            print(i, x-i)
            break