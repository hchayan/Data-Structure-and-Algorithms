import sys

x = sys.stdin.readline().rstrip()

num = [0,1,2,3,4,5,6,7,8,9]
ans = 1
for i in x:
    if int(i) in num:
        num.pop(num.index(int(i)))
    else:
        if int(i) == 6 and 9 in num:
            num.pop(num.index(9))
        elif int(i) == 9 and 6 in num:
            num.pop(num.index(6))
        else:
            ans += 1
            num += [0,1,2,3,4,5,6,7,8,9]
            num.pop(num.index(int(i)))
print(ans)


