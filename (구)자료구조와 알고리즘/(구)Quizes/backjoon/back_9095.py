# 우선 규칙찾기
"""
1일때, 1
2
4
7
13
24
44 ...
"""
# 규칙 : n일때, (n-1) +(n-2) + (n-3)이 해당값
# 그리고 여러 테스트 케이스를 받아서 실행하므로
# 전에 실행했던 결과를 저장해두고 이용하는 방법으로 까지 개선.
import sys

lis = [0,1,2,4]  # n=1,2,3때 초기값.
for i in range(int(sys.stdin.readline().rstrip())):
    n = int(sys.stdin.readline().rstrip())
    if len(lis) > n:
        print(lis[n])
    else:
        for x in range(len(lis),n+1):
            lis.append(lis[x-1]+lis[x-2]+lis[x-3])
        print(lis[n])