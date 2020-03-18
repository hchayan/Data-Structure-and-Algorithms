
x = int(input())

cnt = -1
i = 0
while (cnt != x):
    tmp = 10
    cur = True
    for j in str(i):
        if tmp > int(j):
            tmp = int(j)
        else:
            cur = False
            break

    if cur == True:
        cnt += 1

    i+=1

print(i-1)
