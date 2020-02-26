# 주어지는 숫자 5개에서 4개 뽑는 거니 최대값 - 최소값 하면 됨
def miniMaxSum(arr):
    sums = sum(arr)
    print(sums-max(arr), sums-min(arr))


miniMaxSum([1,2,3,4,5])