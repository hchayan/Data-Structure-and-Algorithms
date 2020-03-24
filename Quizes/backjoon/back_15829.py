
n = int(input())
ans = 0
string = list(input())

for i in range(n):
    ans += (ord(string[i])-96) * (31 ** i)
print(ans)