import sys
import itertools
def gcd(a,b):
    if a%b!=0:
        return gcd(b, a%b)
    else:
        return b

n = int(sys.stdin.readline().rstrip())
for nn in range(n):
    x = list(sys.stdin.readline().rstrip().split())
    ans=0
    for i, j in list(itertools.combinations(x[1:], 2)):
        ans+=gcd(int(j), int(i))

    print(ans)




