def solution(citations):
    citations.sort(reverse=True)
    answer = 0
    for i in citations:
        if i <= answer:
            break
        answer+=1
    return answer