import sys

x = sys.stdin.readline().rstrip()

ans = ""
for i in x:
    ans += str(bin(int(i))[2:]).zfill(3)
print(int(ans))