# 우선 각 경우에서 최소값을 뽑아 전에 위치랑 비교해 다르면 적용. 같으면 2번째로 작은 값을 적용하는 구조로 계산

import sys

def find(r,g,b):
    min1 = min(r,g,b)
    if r == min1:
        return min1, min(g,b)
    elif g == min1:
        return min1, min(r,b)
    else:
        return min1, min(r, g)



ans = 0
pos = ""
for n in range(int(sys.stdin.readline().rstrip())):
    lis = list(map(int, sys.stdin.readline().rstrip().split()))
    min1, min2 = find(lis[0], lis[1], lis[2])
    print(min1, min2)
    if pos != min1:
        if min1 == 'r': ans+=lis[0]
        elif min1 == 'g': ans+=lis[1]
        else: ans+=lis[2]
        pos = min1
    else:
        if min2 == 'r': ans+=lis[0]
        elif min2 == 'g': ans+=lis[1]
        else: ans+=lis[2]
        pos = min2
print(ans)

