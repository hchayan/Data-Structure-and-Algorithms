def kangaroo(x1, v1, x2, v2):
    if (x1 <= x2 and v1 <= v2) or (x1 > x2 and v1 > v2):
        return 'NO'
    if abs(x2 - x1) % abs(v2 - v1) != 0:
        return 'NO'
    return 'YES'

print(kangaroo(0, 2, 5, 3))