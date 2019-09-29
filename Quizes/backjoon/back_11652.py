import sys

n = int(sys.stdin.readline().rstrip())

def ans(lis):
    tmp =[]
    for x,y in lis:
        tmp.append((y,x))
    return tmp

dic = {}
for nn in range(n):
    x = int(sys.stdin.readline().rstrip())
    if x in dic:
        dic[x]+=1
    else:dic[x]=1
print(sorted(ans(dic.items()), reverse=True)[0][1])


