graph = {
	1: [2, 3, 4],
	2: [5],
	3: [5],
	4: [],
	5: [6, 7],
	6: [],
	7: [3],
}


# 1. 재귀
def DFS(start_node, visited=[]):
    visited.append(start_node)
    for w in graph[start_node]:
        if not w in visited:
            visited = DFS(w, visited)
    return visited

print(DFS(1))


# 반복
def DFS2(start_node):
    visited = {}

    stack = []  # DFS에서는 스택을 사용
    stack.append(start_node)

    while stack:
        node = stack.pop()
        if node not in visited:
            visited[node] = True
            stack.extend(reversed(graph[node]))   # revered 없으면 오른쪽부터 파고듬
    return list(visited.keys())

print(DFS2(1))



# bfs
def BFS(start_node):
    visited = []

    queue = []   # 큐 형태로 구현 예정
    queue.append(start_node)

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            for w in graph[node]:
                queue.append(w)

    return visited

print(BFS(1))