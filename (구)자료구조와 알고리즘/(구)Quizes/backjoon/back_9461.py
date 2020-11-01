# 우선 값들의 규칙성을 찾아야한다.
# 1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12, 16, 21, 28
# 1, 1, 1, (1+1), 2, (2+1), (3+1), (4+1), (5+2), (7+2), (9+3), (12+4), (16+5), (21+7)

# n번째 수는 n-1번째수에 n-5번째수를 더한 값.

import sys

def find(n):
    tmp = [1,1,1,2,2]
    if n < 6:
        return tmp[n-1]
    else:
        for i in range(5, n):
            tmp.append(tmp[i-1]+tmp[i-5])
        return tmp.pop()

for n in range(int(sys.stdin.readline().rstrip())):
    print(find(int(sys.stdin.readline().rstrip())))


