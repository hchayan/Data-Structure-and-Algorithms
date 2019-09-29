import sys

n = int(sys.stdin.readline().rstrip())

lis = []
for nn in range(n):
    lis.append(sys.stdin.readline().rstrip())

tmp = []
for i in sorted(list(set(lis)), key=lambda leng: (len(leng), leng)):
    print(i)

