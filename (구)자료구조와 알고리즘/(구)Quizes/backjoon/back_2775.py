import sys

n = int(sys.stdin.readline().rstrip())
house = [[0]*15 for i in range(15)]

for i in range(15):
    house[0][i] = i+1
    house[i][0] = 1

for i in range(1,15):
    for j in range(1,15):
        house[i][j] = house[i-1][j]+house[i][j-1]

for i in range(n):
    a = int(sys.stdin.readline().rstrip())
    b = int(sys.stdin.readline().rstrip())
    print(house[a][b-1])



'''
def person(a,b):  # 재귀함수로 푸는법
    if b == 1:
        return 1
    if a == 0:
        return b
    return person(a-1,b)+person(a,b-1)
'''