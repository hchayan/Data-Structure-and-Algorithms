


import sys

n = int(sys.stdin.readline().rstrip())

cnt = 1
tmp = []
ans = []
for nn in range(n):
    a = int(sys.stdin.readline().rstrip())

    while cnt <= a:
        tmp.append(cnt)
        ans.append("+")
        cnt+=1

    if tmp[-1] == a:
        tmp.pop()
        ans.append("-")
    else:
        print("NO")
        exit()

print('\n'.join(ans))


