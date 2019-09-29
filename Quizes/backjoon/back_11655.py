import sys

ans = ""
for i in sys.stdin.readline().rstrip():
    ord_i = ord(i)

    if ord_i >=97 and ord_i <= 122:
        if ord_i+13 > 122:
            ord_i -= 13
        else:
            ord_i += 13

    elif ord_i >=65 and ord_i <= 90:
        if ord_i+13 > 90:
            ord_i -=13
        else:
            ord_i += 13

    ans+=chr(ord_i)
print(ans)