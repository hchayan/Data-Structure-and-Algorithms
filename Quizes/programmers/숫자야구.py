from itertools import permutations

def check(ans, num, s, b):
    t_s, t_b = 0, 0
    for i in range(3):
        if ans[i] == num[i]:
            t_s += 1
        else:
            if ans[i] in num:
                t_b += 1

    if t_s == s and t_b == b:
        return True
    else:
        return False


def solution(baseball):
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    items = list(map(''.join, permutations(nums, 3)))


    for num, s, b in baseball:
        tmp = []
        for item in items:
            if check(str(num), item, s, b):
                tmp.append(item)
        items = tmp


    return len(items)


print(solution([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]))