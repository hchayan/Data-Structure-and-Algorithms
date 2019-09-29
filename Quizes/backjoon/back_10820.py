import sys
print(*[1, 3, 2, 5])
for strr in sys.stdin:
    ans = ['0','0','0','0']
    for i in strr:
        ord_i = ord(i)
        if ord_i >= 97 and ord_i <=122:
            ans[0] = str(int(ans[0])+1)
        elif ord_i >= 65 and ord_i <=90:
            ans[1] = str(int(ans[1])+1)
        elif ord_i >= 48 and ord_i <= 57:
            ans[2] = str(int(ans[2])+1)
        elif i == " ":
            ans[3] = str(int(ans[3])+1)
    print(' '.join(ans))


