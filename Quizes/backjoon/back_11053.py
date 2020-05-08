
N = int(input())
nums = list(map(int, input().split()))

dp = [1]

for i in range(1,len(nums)):
    tmp = 0
    for j in range(i):
        if nums[j] < nums[i]:
             tmp = max(tmp, dp[j])
    dp.append(tmp + 1)

print(max(dp))

'''
total = 0
prev = 0
ans = 0
for n in range(len(nums)):
    if prev <= nums[n]:
        total += nums[n]
        prev = nums[n]
        ans += 1
    else:
        if total < nums[n]:
            total = nums[n]
            prev = nums[n]
            ans += 1

print(ans)
'''