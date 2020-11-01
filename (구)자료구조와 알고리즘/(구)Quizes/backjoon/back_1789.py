
n = int(input())
ans = 0
i = 1
while True:
    ans+=i
    if ans+i+1 > n:
        break
    i += 1

print(i)