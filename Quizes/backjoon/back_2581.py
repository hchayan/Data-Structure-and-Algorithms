
def isPrime(a):
    if a < 2:
        return False

    i = 2
    while i*i <= a:
        if(a%i == 0):
            return False
        i+=1
    return True

import sys
x = int(sys.stdin.readline().rstrip())
y = int(sys.stdin.readline().rstrip())
res = 0
minn = -1
for i in range(x,y+1):
    if isPrime(i) == True:
        res += i
        if minn == -1:
            minn = i

if minn != -1:
    print(res)
print(minn)
