import sys

x, n = map(int,sys.stdin.readline().rstrip().split())

tmp_x = x
cnt = 0
while tmp_x > n:
    tmp_x//=n
    cnt+=1

for i in range(cnt,-1,-1):

print(cnt)

