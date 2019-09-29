# 하도 시간초과떠서 답 보니 C와 코드 같은데도 시간초과... Dp로 풀래..

import sys

def check(command,lis):
    for i in command:
        if i =="R":
            lis.reverse()

        elif i=="D":
            if len(lis)==0:
                return "error"
            lis = lis[1:]

    return list(map(int,lis))


n = int(sys.stdin.readline().rstrip())

for nn in range(n):
    command = sys.stdin.readline().rstrip()
    x = int(sys.stdin.readline().rstrip())
    lis= list(sys.stdin.readline().rstrip().split(",")[1:-1])

    print(check(command, lis))


