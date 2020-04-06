
students = []
N = int(input())

for i in range(N):
    students.append(list(map(int, input().split())))

cnt = [[0]*5]*N

for nn in range(N):
    sa, sb = students[nn]
    print(sa, sb, nn)

    cnt[nn][sa-1] += 1
    cnt[nn][sb-1] += 1

    print(cnt)
print(cnt)