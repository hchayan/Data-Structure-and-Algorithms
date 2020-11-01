def maxProfit(nums):
    if len(nums) == 0:
        return 0
    minn = nums[0]
    ans = 0
    for i, num in enumerate(nums):
        if minn > num:
            minn = num
        else:
            ans = max(ans, num - minn)
    return ans



print(maxProfit([7,1,5,3,6,4]))