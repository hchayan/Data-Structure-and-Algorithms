import sys

lis = []
x = sys.stdin.readline().rstrip()

for i in range(len(x)):
    lis.append(x[i:])

lis.sort()

for i in lis:
    print(i)
