def solution(n, computers):
    answer = 0
    visited = [0 for i in range(n)]

    def dfs(computers, visited, start):
        stack = [start]
        while stack:
            node = stack.pop()
            if visited[node] == 0:  # not in visited
                visited[node] = 1

                #stack.extend(reversed(graph[node])))
                for i in range(len(computers)): #전체검색
                    if computers[node][i] == 1 and visited[i] == 0: # 연결되있고 방문 안했으면.
                        stack.append(i)

    i = 0
    while 0 in visited:
        if visited[i] == 0:
            dfs(computers, visited, i)
            answer += 1
        i+=1
    return answer
