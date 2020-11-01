x, length = map(int, input().split())

trees = list(map(int, input().split()))


start, end = 0, max(trees)

while start <= end:
    tmp = 0
    mid = (start + end) // 2
    for tree in trees:
        if tree > mid:
            tmp += (tree-mid)
    if tmp >= length:
        start = mid + 1
    else:
        end = mid - 1

print(end)