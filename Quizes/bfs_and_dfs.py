
graph = {
    'A': ['B', 'C'],
    'B': ['A','D','E'],
    'C': ['A','F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
    }


from queue import Queue

# BFS
def bfs(graph, start_node):
    visited = {}                # 방문했던 노드목록 (dic, set 형태로 구현해야 효율
    q = Queue()                 # bfs는 queue, dfs는 stack : 유일한 차이점!!!

    q.put(start_node)

    while q.qsize() > 0:
        node = q.get()   # 큐 특징. FIFO
        if node not in visited:
            visited[node] = True
            for nextNode in graph[node]:
                q.put(nextNode)

    return visited.keys()

print(bfs(graph, 'A'))



# DFS
def dfs(graph, start_node):
    visited = {}
    stack = list()

    stack.append(start_node)
    while stack:
        node = stack.pop()
        if node not in visited:
            visited[node] = True
            stack.extend(reversed(graph[node]))   # revered 없으면 오른쪽부터 파고듬

    return visited.keys()

print(dfs(graph, 'A'))
