import sys

n = sys.stdin.readline().rstrip()

ans = []
for i in n:
    ans.append(i)

ans.sort(reverse=True)

print(''.join(ans))