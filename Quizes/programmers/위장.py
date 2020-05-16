def solution(clothes):
    dict = {}
    for name, cate in clothes:
        if cate not in dict.keys():
            dict[cate] = 2
        else:
            dict[cate] += 1

    ans = 1
    for i in dict.values():
        ans *= i

    return ans - 1