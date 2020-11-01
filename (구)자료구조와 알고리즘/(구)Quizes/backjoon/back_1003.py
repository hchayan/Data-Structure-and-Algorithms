# 재귀는 함수를 불러오는 획수가 기하급수적으로 증가(2^n)해서 느려짐..

# 이문제는 규칙성을 찾아야된다.
'''
n = 0일때, 1 0
n =1     , 0 1
n = 2    , 1 1
n = 3    , 1 2
n = 4    , 2 3
n = 5    , 3 5
n = 6    , 5 8
'''
# 규칙성 : 0, 1의 개수는 n = 2일때부터 피보나치 값대로 증가함을 볼수 있다. 이를 이용해 계산식을 만든다.

import sys

for nn in range(int(sys.stdin.readline().rstrip())):
    x = int(sys.stdin.readline().rstrip())
    if x == 0: print(1, 0)
    elif x== 1: print(0, 1)
    else:
        zero, one = 1, 1
        for i in range(x-2):
            zero, one = one, zero+one
        print(zero, one)