# 원리)
# x, y는 1~n, 1~n의 모든 좌표
# _draw_ 함수에 모든 x,y좌표 넣음
# _draw_ 함수에서 들어온 x,y좌표
import sys

n = int(sys.stdin.readline().rstrip())

def draw_star(n):
    for x in range(n):
        for y in range(n):
            _draw_(x,y)
        print("")


def _draw_(x,y):
    while y>0:
        if (x%3==1 and y%3==1):
            print(" ",end="")
            return
        x//=3
        y//=3

    print("*",end="")

draw_star(n)



