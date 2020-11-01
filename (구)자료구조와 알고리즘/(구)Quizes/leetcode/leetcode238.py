def productExceptSelf(nums):
    ans = [1]
    for i in range(len(nums)-1):
        ans.append(ans[i]*nums[i])

    ini = 1
    for i in range(len(nums)-1, -1, -1):
        ans[i] *= ini
        ini *= nums[i]


    print(ans)

productExceptSelf([1,2,3,4])
productExceptSelf([0,1])