import math

n = int(input())

ans_list = [0] * (n+1)

for i in range(1,n+1):
    if i < 4:
        ans_list[i] = i
    else:
        tmp = i
        for j in range(2,int(math.sqrt(i))+1):
            tmp = min(tmp, ans_list[i-j*j]+1)
        ans_list[i] = tmp
print(ans_list[n])