

for nn in range(10):
    maxx = int(input())
    lis = list(map(int, input().split()))
    lis.sort()
    i = 0
    while(i != maxx):




        print(i,r,l, lis[r], lis[l], lis)

    print(lis[r] - lis[l])
