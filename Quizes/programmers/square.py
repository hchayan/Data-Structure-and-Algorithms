# 문제에서 각 케이스를 분석 후 패턴 파악후 식으로 도출


def gcd(a, b):
    ans = 1
    if a < b:
        a, b = b, a

    while b != 0:
        ans = a % b
        a, b = b, ans
    return a


def solution(w, h):
    answer = 1
    g = gcd(w, h)

    if w == h:
        answer = w * h - w

    elif g == 1:
        answer = (w - 1) * (h - 1)

    else:
        answer = (w // g - 1) * (h // g - 1) * g + (w - w // g) * h

    return answer