
lis = []
for i in range(int(input())):
    lis.append(list(map(int,input().split())))


ans = []
for w, h in lis:
    i = 1
    for wi, hi in lis:
        if w < wi and h < hi:
            i +=1
    ans.append(str(i))

print(' '.join(ans))