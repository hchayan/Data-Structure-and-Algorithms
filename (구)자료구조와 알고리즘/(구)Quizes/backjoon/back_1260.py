from queue import Queue

n,m,v = map(int, input().split())

nodes = {}

for i in range(n):
    nodes[i+1] = []   # 정점은 1~n개가 있으므로 미리생성해줘야함 (런타임 에러 원인...)


for i in range(m):
    key, value = map(int, input().split())

    # 그래프인 만큼 쌍방향 연결
    nodes[key].append(value)
    nodes[value].append(key)

# 노드의 값중 작은 값부터 select 한다해서 정렬.
for node in nodes.values():
    node.sort()


# 1. DFS - stack을 이용
def dfs(nodes, start_node):
    visited = {}
    stack = list()

    stack.append(start_node)

    while stack:
        node = stack.pop()
        if node not in visited:
            visited[node] = True
            stack.extend(reversed(nodes[node]))

    return " ".join(map(str, visited.keys()))

print(dfs(nodes, v))

# 2. bfs - queue를 이용
def bfs(nodes, start_node):
    visited = {}
    q = Queue()  # 큐처럼 사용

    q.put(start_node)
    try:
        while q.qsize() > 0:
            node = q.get()  # 큐 특징 FIFO
            if node not in visited:
                visited[node] = True
                for nextNode in nodes[node]:
                    q.put(nextNode)
    except:  # 런타임 에러 발생 이유 2
        return

    return " ".join(map(str, visited.keys()))


print(bfs(nodes, v))