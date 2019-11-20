
def check(chmi, i):
    print(chmi[i])
    tmp = 0
    mul = 1
    if i == len(chmi)-1:
        return 0

    if chmi[i] == "(":
        tmp += check(chmi, i+1)
    elif chmi[i] == ")":
        return 0
    elif chmi[i] == "H":
        tmp = 1
    elif chmi[i] == "C":
        tmp = 12
    elif chmi[i] == "O":
        tmp = 16
    else:
        mul = int(chmi[i])

    return check(chmi, i+1) + tmp*mul





print(check(input(), 0))

