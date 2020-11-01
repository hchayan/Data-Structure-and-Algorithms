
quads = []
for i in range(int(input())):
    if i == 0:
        quads.append(1)
    elif i == 1:
        quads.append(3)
    else:
        quads.append(quads[i-1] + quads[i-2] * 2)
print(quads.pop()%10007)