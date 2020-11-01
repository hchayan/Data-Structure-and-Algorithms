import sys

x = int(sys.stdin.readline().rstrip())
flag = False
for i in range(x):
    tmp_i = i
    tmp = i
    while tmp_i%10 != tmp_i:
        tmp+=tmp_i%10
        tmp_i//=10
    tmp+=tmp_i%10

    if tmp == x:
        flag = True
        break

if flag==True:
    print(i)
else:
    print(0)

