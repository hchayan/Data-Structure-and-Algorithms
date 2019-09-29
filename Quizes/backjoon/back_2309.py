import sys

tmp = []
for i in range(9):
    x = int(sys.stdin.readline().rstrip())
    tmp.append(x)

tmp.sort()
s = sum(tmp)-100

flag = False
for i in range(8):
    for j in range(i,9):
        if tmp[i]+tmp[j] == s:
            tmp.remove(tmp[i])
            tmp.remove(tmp[j-1])
            flag = True
            break
    if flag==True:
        break

for t in tmp:
    print(t)


