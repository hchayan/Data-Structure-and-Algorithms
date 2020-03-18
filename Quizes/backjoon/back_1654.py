




x, length = map(int, input().split())
lines = []

for i in range(x):
    lines.append(int(input()))

start, end = 1, max(lines)

while start <= end:
    mid = (start+end)//2
    tmp = 0
    for line in lines:
        tmp += line // mid

    if tmp >= length:
        start = mid + 1
    else:
        end = mid -1
print(end)