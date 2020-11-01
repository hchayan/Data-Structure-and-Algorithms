
for n in range(int(input())):
    score = [0]*101
    case = int(input())
    for i in map(int,input().split()):
        score[i]+=1

    tmp = 0
    ans = 0
    for i in range(len(score)):
        if tmp <= score[i]:
            tmp = score[i]
            ans = i
    print('#{} {}'.format(case, ans))
