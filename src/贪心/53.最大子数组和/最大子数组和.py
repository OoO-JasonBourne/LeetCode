def maxSubArray(nums):
    sum, res = 0, 0
    # 全为负数的情况排序，最大和即为最大（绝对值最小）的那个负数
    nums_sorted = sorted(nums)
    if nums_sorted[-1] < 0:
        return nums_sorted[-1]
    # 存在正数的情况
    for i in range(len(nums)):
        sum += nums[i]
        res = max(sum, res)
        if sum < 0:
            sum = 0
    return res

print(maxSubArray([-1, 0, 8, -7]))