N,M = map(int, input().split())

nodes = {}

for _ in range(M):
    key, value = map(int, input().split())

    if key not in nodes.keys():
        nodes[key] = [value]
    else:
        nodes[key] += [value]

    if value not in nodes.values():
        nodes[value] = [key]
    else:
        nodes[value] += [key]

print(nodes)

to_visit = nodes.keys()
visited = []
start_node = nodes.keys()[0]

while len(to_visit) == 0:

    stack = list()   #dfs




stack.append(nodes.keys()[0])

while stack:

