import sys

dic = []
for nn in range(int(sys.stdin.readline().rstrip())):
    y, x = map(int, sys.stdin.readline().rstrip().split())
    dic.append([x,y])

for x, y in sorted(dic):
    print(y, x)