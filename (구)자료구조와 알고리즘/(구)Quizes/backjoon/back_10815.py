M = int(input())
lis = list(map(int, input().split()))
lis.sort()

N = int(input())

ans = []
for i in map(int, input().split()):
    start, end = 0, len(lis)-1
    tmp = 0
    while start <= end:
        mid = (start + end) // 2
        if lis[mid] == i:
            tmp = 1
            break
        if lis[mid] < i:
            start = mid + 1
        else:
            end = mid - 1

    ans.append(tmp)
print(' '.join(map(str,ans)))