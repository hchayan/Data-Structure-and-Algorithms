
for nn in range(10):
    leng = int(input())
    lis = list(map(int, input().split()))
    ans = 0
    for i in range(2,len(lis)-2):
        if lis[i] <= lis[i+1] or lis[i] <= lis[i+2] or lis[i] <= lis[i-1] or lis[i] <= lis[i-2]:
            continue
        else:
            ans += (lis[i] - max(lis[i+1], lis[i+2], lis[i-1], lis[i-2]))
    print('#{} {}'.format(nn+1,ans))

