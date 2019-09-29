import sys


cnt = 0
ans = ""
tmp = 0
x = sys.stdin.readline().rstrip()
for i in x[::-1]:
    if cnt==3:
        ans= str(tmp) +ans
        cnt = 1
        tmp = int(i)
    else:
        tmp += int(i)*(2**cnt)
        cnt+=1

print(str(tmp) +ans)
