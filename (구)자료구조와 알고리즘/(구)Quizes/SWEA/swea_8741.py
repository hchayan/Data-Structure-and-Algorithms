
for n in range(int(input())):
    ans = ''
    for i in input().split():
        ans += i[0].upper()
    print('#{} {}'.format(n+1,ans))
