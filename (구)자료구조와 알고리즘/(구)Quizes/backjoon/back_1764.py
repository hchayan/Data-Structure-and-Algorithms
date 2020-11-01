N, M = map(int, input().split())

lis =[]
for i in range(N):
    lis.append(input())

lis.sort()

ans = 0
ans_list = []
for i in range(M):
    tmp = input()

    start, end = 0, len(lis)-1

    while start <= end:
        mid = (start + end) // 2
        if lis[mid] == tmp:
            ans += 1
            ans_list.append(tmp)
            break
        if lis[mid] < tmp:
            start = mid + 1
        else:
            end = mid - 1

print(ans)
ans_list.sort()
for a in ans_list:
    print(a.rstrip())