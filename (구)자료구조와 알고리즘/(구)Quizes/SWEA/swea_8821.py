
for n in range(int(input())):
    lis = [0]*10
    for i in input():
        if lis[int(i)] == 0:
            lis[int(i)] = 1
        else:
            lis[int(i)] = 0
    print("#{} {}".format(n+1, lis.count(1)))