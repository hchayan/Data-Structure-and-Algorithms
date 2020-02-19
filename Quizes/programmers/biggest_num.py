
def solution(numbers):
    tmp = []
    for n in numbers:
        if len(str(n)) == 1:
            tmp.append([str(n*1111), 3])
        elif len(str(n)) == 2:
            tmp.append([str(n)+str(n)[0]*2, 2])
        elif len(str(n)) == 3:
            tmp.append([str(n)+str(n)[0], 1])
        else:
            if n == 1000:
                tmp.append(["1000", 0])
            else:
                tmp.append(["0000", 3])

    tmp.sort(reverse=True)

    ans = ''
    for n, i in tmp:
        ans += n[:4-i]
    return str(int(ans))



print(solution([0,0,0,1000]))
print(solution([0,0,1000,0]))
print(solution([0, 50, 50, 0, 5]))



