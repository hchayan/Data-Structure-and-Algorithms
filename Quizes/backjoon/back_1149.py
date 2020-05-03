import sys
costs = [[0,0,0]]

for i in range(int(sys.stdin.readline())):
    costs.append(list(map(int, sys.stdin.readline().split())))
    costs[i + 1][0] = min(costs[i][1], costs[i][2]) + costs[i+1][0]
    costs[i + 1][1] = min(costs[i][0], costs[i][2]) + costs[i+1][1]
    costs[i + 1][2] = min(costs[i][0], costs[i][1]) + costs[i+1][2]

print(min(costs[len(costs)-1]))



# 재귀 방식..
"""
def lowest(costs, leng,  pos):
    if leng >= len(costs) - 1:
        if pos == 0:
            return min(costs[leng][1], costs[leng][2])
        elif pos == 1:
            return min(costs[leng][0], costs[leng][2])
        else:
            return min(costs[leng][0], costs[leng][1])

    if pos == 0:
        return costs[leng][0] + min(lowest(costs, leng+1, 1), lowest(costs, leng+1, 2))
    elif pos == 1:
        return costs[leng][1] + min(lowest(costs, leng+1, 0), lowest(costs, leng+1, 2))
    else:
        return costs[leng][2] + min(lowest(costs, leng+1, 0), lowest(costs, leng+1, 1))





print(min(lowest(costs, 0, 0), lowest(costs, 0, 1), lowest(costs, 0, 2)))
"""