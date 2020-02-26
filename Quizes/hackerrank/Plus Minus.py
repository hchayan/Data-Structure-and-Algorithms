
def plusMinus(arr):
    m, z, p = 0, 0, 0
    for i in arr:
        if i < 0:
            m += 1
        elif i > 0:
            p += 1
        else:
            z += 1
    print(round(p/len(arr), 6))
    print(round(m / len(arr), 6))
    print(round(z / len(arr), 6))

print(plusMinus([-4, 3, -9, 0, 4, 1]))