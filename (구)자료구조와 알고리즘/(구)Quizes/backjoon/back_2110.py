import sys

N, router = map(int, sys.stdin.readline().split())

houses = []
for i in range(N):
    houses.append(int( sys.stdin.readline()))

houses.sort()


start, end = 1, houses[len(houses)-1] - houses[0]   # 가장 멀리있는 집들간의 거리

while start <= end:
    mid = (start + end) // 2

    # 필요 라우터 개수 카운트
    tmp = 1
    cur = houses[0]
    for i in range(N):
        if mid <= (houses[i]-cur):
            tmp += 1
            cur = houses[i]
    if tmp >= router:
        start = mid + 1
    else:
        end = mid - 1

print(end)