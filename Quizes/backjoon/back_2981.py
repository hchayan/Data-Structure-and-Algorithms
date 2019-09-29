import sys

n = int(sys.stdin.readline().rstrip())
tmp=[]
for i in range(n):
    x = int(sys.stdin.readline().rstrip())
    tmp.append(x)

min_tmp = min(tmp)
i=2
ans =[]
while i <= min_tmp:
    flag = True
    namu = tmp[0]%i
    for t in tmp:
      if t%i != namu:
        flag=False
        break
    if flag ==True:
        ans.append(str(i))
    i+=1
print(" ".join(ans))