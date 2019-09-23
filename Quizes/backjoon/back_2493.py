import sys

n = int(sys.stdin.readline().rstrip())

lis = list(map(int, sys.stdin.readline().rstrip().split(" ")))

ans = []

for i in range(len(lis)):
    flag = False
    for j in range(i,-1,-1):
        if lis[i] < lis[j]:
            ans.append(j+1)
            flag = True
            break
    if flag == False:
        ans.append(0)

print(' '.join(map(str,ans)))


