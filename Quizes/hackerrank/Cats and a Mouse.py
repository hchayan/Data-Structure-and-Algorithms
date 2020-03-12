def catAndMouse(x, y, z):
    tmp1, tmp2 = abs(x-z), abs(y-z)
    if tmp1 < tmp2:
        return "Cat A"
    elif tmp1 > tmp2:
        return "Cat B"
    return "Mouse C"

print(catAndMouse(1, 2, 3))