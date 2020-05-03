import sys

N = int(sys.stdin.readline())
stairs = []
for _ in range(N):
    stairs.append(int(sys.stdin.readline()))

ans =[]

for i in range(N):
    if i == 0:
        ans.append(stairs[0])
    elif i == 1:
        ans.append(stairs[0] + stairs[1])
    elif i == 2:
        ans.append(max(stairs[1] + stairs[2], stairs[0] + stairs[2]))
    else:
        ans.append(max(ans[i-3] + stairs[i-1] + stairs[i], ans[i-2] + stairs[i]))

print(ans.pop())


