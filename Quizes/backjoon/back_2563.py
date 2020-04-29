paper = {}

for i in range(int(input())):
    a, b = map(int, input().split())
    for x in range(a, a+10):
        for y in range(b, b+10):
            if (x,y) not in paper.keys():
                paper[(x,y)] = 1

print(sum(paper.values()))