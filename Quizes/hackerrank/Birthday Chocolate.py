def birthday(s, d, m):
    cnt = 0
    for i in range(len(s)-m+1):
        tmp = 0
        for a in range(i, i+m):
            tmp += s[a]
        if tmp == d:
            cnt += 1
    return cnt


print(birthday([1, 2, 1, 3, 2], 3, 2))