# 动态规划五部曲
"""
1.确定dp数组和下标含义
2.确定递推公式
3.初始化
4.遍历顺序
5举例
"""
def selectNotes(nums):
    n = len(nums)
    dp = [0 for i in range(n)]
    dp_count = [1 for i in range(n)]
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        if dp[i - 1] < dp[i - 2] + nums[i]:
            dp_count[i] = dp_count[i - 2] + 1
        else:
            dp_count[i] = dp_count[i - 1]

    return [dp[n - 1], dp_count[n - 1]]




nums = [1, 2, 3, 1]
print(selectNotes(nums))
