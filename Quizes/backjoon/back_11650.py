import sys

dic = []
for nn in range(int(sys.stdin.readline().rstrip())):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    dic.append([x,y])

for x, y in sorted(dic):
    print(x, y)