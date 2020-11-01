def breakingRecords(scores):
    maxx = minn = scores[0]
    max_cnt = min_cnt = 0

    for score in scores:
        if maxx < score:
            maxx = score
            max_cnt += 1
        if minn > score:
            minn = score
            min_cnt += 1

    return [max_cnt, min_cnt]


print(breakingRecords([3, 4, 21, 36, 10, 28, 35, 5, 24, 42]))