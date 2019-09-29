import sys

n = int(sys.stdin.readline().rstrip())

x = list(map(int,sys.stdin.readline().rstrip().split()))

for nn in range(1, n):
    i = 2
    tmp = x[0]
    while i <= x[nn]:
        if tmp%i==0 and x[nn]%i==0:
            tmp//=i
            x[nn]//=i
            i-=1
        i+=1
    print(str(tmp)+"/"+str(x[nn]))
