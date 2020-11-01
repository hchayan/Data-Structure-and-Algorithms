# 재귀로 안푸는게 효율적이지만 재귀로 풀어봄

def find(N,x,y):
    global res, flag
    if flag == True:
        return

    if N == 2:
        if x == r and y == c:
            flag = True
            return
        res +=1
        if x == r and y+1 == c:
            flag = True
            return
        res += 1
        if x+1 == r and y == c:
            flag = True
            return
        res += 1
        if x+1 == r and y+1 == c:
            flag = True
            return
        res += 1

        return


    find(N//2, x, y)
    find(N//2, x, y + N//2)
    find(N//2, x + N//2 , y)
    find(N//2, x + N//2, y + N//2)

import sys
N, r, c = map(int,sys.stdin.readline().rstrip().split())
res = 0
flag = False

find(2**N,0,0)
print(res)