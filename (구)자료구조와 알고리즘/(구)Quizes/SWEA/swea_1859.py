
for nn in range(int(input())):
    i = int(input())-1
    lis = list(map(int,input().split()))
    ans = 0
    k = lis[len(lis)-1]

    for j in range(i,-1,-1):
        if lis[j] < k:
            ans += (k-lis[j])
        else:
            k = lis[j]
    print("#" + str(nn + 1) + " " + str(ans))




'''
    for j in range(i):
        ans += (k - lis[j])
        if lis[j] == k:
            k = max(lis[j+1:])
        print(ans, k, j)
        '''




