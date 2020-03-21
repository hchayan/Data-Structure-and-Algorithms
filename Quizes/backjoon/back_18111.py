x, y, b = map(int, input().split())
grounds = []
for i in range(x):
    grounds += list(map(int, input().split()))

time, height = 256*x*y*2, -1
for i in range(257):
    tmp_time = 0
    tmp_blocks = 0
    for ground in grounds:
        if ground > i:
            tmp_time += 2*(ground-i)
        elif ground < i:
            tmp_time += (i-ground)
        tmp_blocks += (i - ground)
    if tmp_time <= time and tmp_blocks <= b:
        time = tmp_time
        height = i

print(time, height)
