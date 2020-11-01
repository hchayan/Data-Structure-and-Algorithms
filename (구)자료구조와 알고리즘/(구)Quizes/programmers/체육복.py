
def solution(n, lost, reserve):
    answer = 0
    tmp = [1] * 5
    for i in lost:
        tmp[i-1] = 0
    for i in reserve:
        tmp[i-1] = 2

    for i in range(n):
        if tmp[i] == 0:
            if i == 0:
                if tmp[i+1] == 2:
                    tmp[i]+=1
                    tmp[i+1]-=1
            elif i == n-1:
                if tmp[i-1] == 2:
                    tmp[i]+=1
                    tmp[i-1]-=1
            else:
                if tmp[i-1] == 2:
                    tmp[i]+=1
                    tmp[i-1]-=1
                elif tmp[i+1] == 2:
                    tmp[i]+=1
                    tmp[i+1]-=1

    return n - tmp.count(0)


print(solution(5, [2,4], [1,3,5]))
print(solution(5, [2,4], [3]))
print(solution(3, [3], [1]))