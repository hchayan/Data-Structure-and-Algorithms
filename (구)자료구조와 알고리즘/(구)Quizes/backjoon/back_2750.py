import sys

lis = []

for i in range(int(sys.stdin.readline().rstrip())):
    lis.append(int(sys.stdin.readline().rstrip()))

for i in range(len(lis)):
    for j in range(i,len(lis)):
        if lis[i] > lis[j]:
            lis[i], lis[j] = lis[j], lis[i]

for i in lis:
    print(i)