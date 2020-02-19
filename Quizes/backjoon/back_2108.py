
nums = []
for i in range(int(input())):
    nums.append(int(input()))

# 산술 평균
print(round(sum(nums)/len(nums)))

# 중앙값
nums.sort()
if len(nums)%2 == 1:
    print(nums[len(nums)//2])
else:
    print((nums[len(nums)//2] + nums[len(nums)//2+1]) / 2)

# 최빈값
dic = {}
for n in nums:
    if n not in dic:
        dic[n] = 1
    else:
        dic[n] += 1

sorted(dic.values())
maxv = max(dic.values())
tmp = []
for k, v in dic.items():
    if v == maxv:
        tmp.append(k)

if len(tmp) < 2:
    print(tmp[0])
else:
    print(tmp[1])

# 범위
print(nums[len(nums)-1] - nums[0])
