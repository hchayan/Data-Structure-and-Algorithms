import sys
for nn in range(int(sys.stdin.readline().rstrip())):
    n, x = map(int,sys.stdin.readline().rstrip().split())
    lis = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    cnt = 0
    while True:
        maxx = max(lis)
        if maxx != lis[0]:
            lis = lis[1:]+[lis[0]]
            x = (x-1)%len(lis)

        else:
            cnt +=1
            lis.pop(0)
            if x ==0:
                print(cnt)
                break;
            x-=1
