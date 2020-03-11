def countingValleys(n, s):
    cnt, ans = 0, 0
    for i in s:
        tmp = False
        if cnt < 0:
            tmp = True

        if i == 'U':
            cnt += 1
        else:
            cnt -= 1

        if cnt >= 0 and tmp == True:
            ans += 1
    return ans

print(countingValleys(8, 'UDDDUDUU'))