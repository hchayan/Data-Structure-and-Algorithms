import math


def hart(num):
    tmp = int(math.floor(math.sqrt(num)))
    for i in range(tmp, 0, -1):
        if i == 1:
            return 0
        if num%i == 0:
            return max(hart(i),hart(num//i)) + 1

print(hart(int(input())))