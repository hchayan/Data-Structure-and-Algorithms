

def birthdayCakeCandles(ar):
    maxx, cnt = 0, 0
    for i in ar:
        if i > maxx:
            maxx = i
            cnt = 1
        elif i == maxx:
            cnt += 1
    return cnt



print([3, 2, 1, 3])