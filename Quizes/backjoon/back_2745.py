import sys

x, n = sys.stdin.readline().rstrip().split()


ans = 0
cnt = 0
for i in x[::-1]:
    if ord(i) >= 65 and ord(i) <= 90:
        ans += (ord(i)-55)*(int(n)**cnt)
    else:
        ans += int(i)*(int(n)**cnt)
    cnt+=1
print(ans)