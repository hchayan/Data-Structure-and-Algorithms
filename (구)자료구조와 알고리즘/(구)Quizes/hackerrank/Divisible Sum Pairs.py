def divisibleSumPairs(n, k, ar):
    cnt = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if (ar[i] + ar[j]) % k == 0:
                cnt += 1
    return cnt

print(divisibleSumPairs(6, 3, [1, 3, 2, 6, 1, 2]))