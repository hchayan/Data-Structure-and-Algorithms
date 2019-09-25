
progresses = [93,30,55]
speeds = [1,30,5]

def solution(progresses, speeds):
    day = []
    for i in range(len(progresses)):
        tmp = (100-progresses[i])//speeds[i]
        if (100-progresses[i])%speeds[i] != 0:
            tmp +=1
        day.append(tmp)

    answer = []
    stand = day[0]
    cnt = 0
    for i in range(len(day)):
        if day[i] > stand:
            answer.append(cnt)
            cnt = 0
            stand = day[i]
        cnt+=1

    if cnt != 0:
        answer.append(cnt)

    return answer


print(solution(progresses,speeds))


# 다른사람 풀이
'''
def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]
'''