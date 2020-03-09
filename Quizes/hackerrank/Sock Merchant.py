def sockMerchant(n, ar):
    dic = {}
    for a in ar:
        if a not in dic:
            dic[a] = 1
        else:
            dic[a] += 1

    ans = 0
    for d in dic.values():
        ans += d//2

    return ans

print(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]))