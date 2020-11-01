# 문제 : https://programmers.co.kr/learn/courses/30/lessons/43237?language=python3

# 구상한 풀이
# 주어진 예산 / 주어진 지방의 개수 의 값을 루트노드로 잡은뒤
# 이 루트 노드를 기준으로 주어진 예


def solution(budgets, M):
    standard = M/len(budgets)

    larger = 0
    for i in budgets:
        if i <= standard:
            M -= i
        else:
            larger += 1

    if larger == 0:
        return max(standard)
    return M//larger






print(solution([120,110,140,150], 485))