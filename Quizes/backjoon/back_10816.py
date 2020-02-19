import sys

n = int(sys.stdin.readline())
n_lis = {}

for i in sys.stdin.readline().split():
    if i not in n_lis:
        n_lis[i] = 1
    else:
        n_lis[i] += 1

m = int(sys.stdin.readline())
ans = []
for i in sys.stdin.readline().split():
    try:
        ans.append(n_lis[i])
    except:
        ans.append(0)

print(' '.join(map(str,ans)))