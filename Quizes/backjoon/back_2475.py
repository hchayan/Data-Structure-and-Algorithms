

ans = 0
for i in list(map(int, input().split())):
    ans += i*i
print(ans%10)