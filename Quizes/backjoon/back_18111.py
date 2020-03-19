x, y, b = map(int, input().split())
ground = []
for i in range(x):
    ground.append(list(map(int, input().split())))

start, end = 0, 257
tmp2 = 256 * x * y * 2

while start <= end:
    if end == 0 or start == 256:
        break
    tmp = 0
    ub = 0
    mid = (start + end) // 2
    for line in ground:
        for block in line:
            if block > mid:
                tmp += (2 * (block-mid))
                ub -= 1
            elif block < mid:
                tmp += (mid-block)
                ub += 1

    print(start, end, tmp, tmp2, ub)
    if ub > b or tmp < tmp2:
        tmp2 = tmp
        end = mid - 1
    else:
        start = mid + 1

print(end)