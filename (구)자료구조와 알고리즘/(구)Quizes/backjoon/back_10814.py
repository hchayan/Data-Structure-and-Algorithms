import sys

ans= []
for i in range(int(sys.stdin.readline().rstrip())):
    x, y= sys.stdin.readline().rstrip().split()
    ans.append([int(x),y])

for x, y in sorted(ans, key=lambda x : x[0]):
    print(x, y)
