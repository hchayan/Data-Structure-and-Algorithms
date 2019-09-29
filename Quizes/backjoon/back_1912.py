import sys

n = int(sys.stdin.readline().rstrip())

x = list(map(int, sys.stdin.readline().rstrip().split()))

ans = 0

for i in range(n):
    temp = x[i]
    for j in range(i+1,n):
        if temp < temp+x[j]:
            temp += x[j]
        else:
            if ans < temp:
                ans = temp
            break

print(ans)


