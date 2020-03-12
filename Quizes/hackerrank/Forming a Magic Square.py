def formingMagicSquare(s):
    magics = [
        [4, 9, 2, 3, 5, 7, 8, 1, 6],
        [8, 3, 4, 1, 5, 9, 6, 7, 2],
        [6, 1, 8, 7, 5, 3, 2, 9, 4],
        [2, 4, 6, 8, 5, 1, 4, 3, 5]
    ]

    tmp = [0, 0, 0, 0]
    for i in range(9):
        if magics[0][i] != s[i]:
            tmp[0] += 1
        if magics[1][i] != s[i]:
            tmp[1] += 1
        if magics[2][i] != s[i]:
            tmp[2] += 1
        if magics[3][i] != s[i]:
            tmp[3] += 1
    print(tmp)
    min_num = 0
    for i in range(4):
        if tmp[i] == min(tmp):
            min_num = i
            break

    ans = 0
    for i in range(9):
        if magics[min_num][i] != s[i]:
            ans += abs(s[i]-magics[min_num][i])

    return ans

print(formingMagicSquare([4, 9, 2, 3, 5, 7, 8, 1, 5]))
print(formingMagicSquare([4, 8, 2, 4, 5, 7, 6 ,1 ,6]))
print(formingMagicSquare([5,3,4,1,5,8,6,4,2]))
print(formingMagicSquare([4,5,8,2,4,1,1,9,7]))