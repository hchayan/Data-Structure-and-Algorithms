import sys
n = int(sys.stdin.readline().rstrip())

x = list(map(int,sys.stdin.readline().rstrip().split()))

x.sort()
print(x[0]*x[len(x)-1])