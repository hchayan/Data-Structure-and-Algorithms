import sys

n = int(sys.stdin.readline().rstrip())

for nn in range(n):
    x, y = map(int,sys.stdin.readline().rstrip().split())

    # 최소공배수 구하는법 : 최대공약수를 유클리드 공식을 이용해 구한후 x*y/최대공약수 로 계산하면된다.
    if x>y:
        tmp_x, tmp_y = x, y
    else:
        tmp_y, tmp_x = x, y

    while tmp_x%tmp_y !=0:
        namu = tmp_x%tmp_y
        tmp_x = tmp_y
        tmp_y = namu
    print(x*y//tmp_y)