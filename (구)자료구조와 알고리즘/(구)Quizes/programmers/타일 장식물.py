
'''
DP 문제 규칙
N = 1 일때 1 + 1 + 1 + 1
N = 2 일때 1 + 1 + 2 + 2
N = 3 일때 2 + 2 + 3 + 3
N = 4 일때 3 + 3 + 5 + 5
...
즉, f(n)이 n번째 피보나치 값일때,
N = n 일때 f(n-1) + f(n-1) + f(n) + f(n) 이라는 규칙이 있음
'''



def solution(N):
    a1, a2 = 0, 1
    for i in range(N):
        a1, a2 = a2, a1 + a2

    return a1 * 2 + a2 * 2