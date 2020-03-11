def getMoneySpent(keyboards, drives, b):
    ans = -1
    for keyboard in keyboards:
        for drive in drives:
            cost = keyboard + drive
            if cost <= b and ans < cost:
                ans = cost
    return ans


print(getMoneySpent([3,1], [5,2,8], 10))