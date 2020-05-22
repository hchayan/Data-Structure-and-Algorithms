import heapq


def solution(scoville, K):
    heapq.heapify(scoville)

    cnt = 0
    while len(scoville) > 1:
        heapq.heappush(scoville, heapq.heappop(scoville) + (heapq.heappop(scoville) * 2))
        cnt += 1
        flag = True
        for i in scoville:
            if i < K:
                flag = False
                break

        if flag:
            break

    if scoville[0] < K:
        return -1
    else:
        return cnt