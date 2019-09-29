import sys

n = int(sys.stdin.readline().rstrip())

ans = 0
for i in range(n):
    x = sys.stdin.readline().rstrip()
    temp = []
    temp_let = x[0]
    flag = False
    for k in x:
        if k != temp_let:
            if k in temp:
                flag = True
                break
            else:
                temp.append(temp_let)
                temp_let = k
    if flag == False:
        ans +=1
print(ans)

