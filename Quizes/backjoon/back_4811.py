import sys

def check(W,H):

    if W == 0:
        return 1

    if lis[W][H] > 0:
        return lis[W][H]

    lis[W][H] = check(W - 1, H + 1)
    if H > 0:
        lis[W][H] += check(W, H - 1)
    return lis[W][H]


lis = [[0]*31 for i in range(31)]
# W=0 이면 return 1, W=1,H=0이면 return 1

a = int(sys.stdin.readline().rstrip())
while a!=0:
    print(check(a, 0))
    a = int(sys.stdin.readline().rstrip())
