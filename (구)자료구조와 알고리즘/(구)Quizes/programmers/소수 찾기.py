from itertools import permutations

def primeNumber(num):
    if num < 2:
        return False
    else:
        i = 2
        while i*i <= num:
            if num % i == 0:
                return False
            i += 1
        return True


def solution(numbers):
    items = []

    for i in range(1, len(numbers) + 1):
        items += list(map(int, map(''.join, permutations(list(numbers),i))))
    items = set(items)

    ans = 0
    for i in items:
        if primeNumber(i):
            ans+=1

    return ans



print(solution("17"))
print(solution("011"))