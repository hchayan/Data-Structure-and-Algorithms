
tri = [[0,0]]
nums = [[0,0]]

for i in range(int(input())):
    tri.append([0] + list(map(int, input().split()))+ [0])
    nums.append([0] *(i+3))


for num in range(1,len(nums)):
    for i in range(1,num+1):
        nums[num][i] = max(nums[num-1][i-1], nums[num-1][i]) + tri[num][i]

print(max(nums[len(nums)-1]))

