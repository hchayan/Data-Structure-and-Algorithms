# 조합 문제. nCm 의 문제임을 알수있다. 순서 존재.

for _ in range(int(input())):
    ans = 1
    n, m = map(int, input().split())

    for i in range(m, m-n, -1):
        ans *= i
    for i in range(n, 0, -1):
        ans //= i
    print(ans)