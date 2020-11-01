def solution(answers):
    answer = []
    p1 = [1, 2, 3, 4, 5] * (len(answers) // 5 + 1)
    p2 = [2, 1, 2, 3, 2, 4, 2, 5] * (len(answers) // 8 + 1)
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (len(answers) // 10 + 1)

    a1, a2, a3 = 0, 0, 0
    for i in range(len(answers)):
        if answers[i] == p1[i]:
            a1 += 1
        if answers[i] == p2[i]:
            a2 += 1
        if answers[i] == p3[i]:
            a3 += 1

    maxx = max(a1, a2, a3)
    if maxx == a1:
        answer.append(1)
    if maxx == a2:
        answer.append(2)
    if maxx == a3:
        answer.append(3)

    return answer