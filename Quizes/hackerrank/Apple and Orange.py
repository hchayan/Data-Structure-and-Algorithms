def countApplesAndOranges(s, t, a, b, apples, oranges):
    ans1, ans2 = 0, 0
    for apple in apples:
        if a + apple >= s and a + apple <= t:
            ans1 += 1
    print(ans1)
    for orange in oranges:
        if b + orange <= t and b + orange >= s:
            ans2 += 1
    print(ans2)


countApplesAndOranges(7, 11, 5, 15, [-2, 2, 1], [5, -6])