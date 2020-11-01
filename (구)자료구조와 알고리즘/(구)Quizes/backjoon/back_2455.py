

maxx = 0
peoples = 0
for _ in range(4):
    i, j = map(int, input().split())
    peoples += (j - i)
    maxx = max(maxx, peoples)

print(maxx)