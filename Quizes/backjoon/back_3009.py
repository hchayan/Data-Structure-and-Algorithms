import sys

posx = []
posy = []
for i in range(3):
    x, y = sys.stdin.readline().rstrip().split()
    if x in posx:
        posx.pop(posx.index(x))
    else:
        posx.append(x)

    if y in posy:
        posy.pop(posy.index(y))
    else:
        posy.append(y)


print(posx[0], posy[0])
