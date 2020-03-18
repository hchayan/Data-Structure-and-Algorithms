x, y = map(int, input().split())
lis = []

for i in range(x):
    lis.append(list(input()))

BW = [[0 for _ in range(y)] for _ in range(x)]
WB = [[0 for _ in range(y)] for _ in range(x)]

# BW 테스트
for i in range(x):
    for j in range(y):
        if (i+j)%2 == 0:
            if lis[i][j] == "B":
                pass
            else:
                BW[i][j] += 1
        else:
            if lis[i][j] == "W":
                pass
            else:
                BW[i][j] += 1

# WB 테스트
for i in range(x):
    for j in range(y):
        if (i+j)%2 == 0:
            if lis[i][j] == "W":
                pass
            else:
                WB[i][j] += 1
        else:
            if lis[i][j] == "B":
                pass
            else:
                WB[i][j] += 1

ans = 64

#BW판 최소값
for i in range(7, x):
    for j in range(7, y):
        tmp_sum = 0
        for p in range(8):
            for q in range(8):
                if BW[i-p][j-q]:
                    tmp_sum += 1
        if tmp_sum <= ans:
            ans = tmp_sum

#WB판 최소값
for i in range(7, x):
    for j in range(7, y):
        tmp_sum = 0
        for p in range(8):
            for q in range(8):
                if WB[i-p][j-q]:
                    tmp_sum += 1
        if tmp_sum <= ans:
            ans = tmp_sum

print(ans)