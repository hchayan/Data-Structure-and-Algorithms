
def getTotalX(a, b):
    cnt = 0
    for i in range(a[len(a)-1] , b[0]+1):
        tmp = True
        for x in a:
            if i%x != 0:
                tmp = False
                break
        for y in b:
            if y%i != 0:
                tmp = False
                break
        if tmp == True:
            cnt += 1
    return cnt



print(getTotalX([2,4], [16,32,96]))