n = int(input())
budgets = list(map(int, input().split()))
tbudget = int(input())

start, end = 0, max(budgets)

while start <= end:
    mid = (start + end) // 2
    tmp = 0
    for budget in budgets:
        if budget > mid:
            tmp += mid
        else:
            tmp += budget
    if tmp <= tbudget:
        start = mid + 1
    else:
        end = mid - 1

print(end)
