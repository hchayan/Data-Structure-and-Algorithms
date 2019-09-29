import sys

n = int(sys.stdin.readline().rstrip())

dic = {}
for nn in range(n):
    x = int(sys.stdin.readline().rstrip())
    if x not in dic:
        dic[x] = 1
    else:
        dic[x] += 1

lis = sorted(list(dic.keys()))

print(int(round((sum(lis)/len(lis)),0)))
print(lis[len(lis)//2])


tmp_max = max(dic.values())
tmp = []
for k, v in dic.items():
    if v == tmp_max:
        tmp.append(k)

if len(tmp)==1:
    print(tmp.pop())
else:
    print(sorted(tmp))
    print(sorted(tmp)[1])

print(lis[len(lis)-1]-lis[0])
