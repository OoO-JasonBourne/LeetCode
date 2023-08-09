class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        动态规划五部曲：
        1. 确定dp数组（dp table）以及下标的含义
        2. 确定递推公式
        3. dp数组如何初始化
        4. 确定遍历顺序
        5. 举例推导dp数组
        """
        # sum, res = 0, 0
        # nums_sorted = sorted(nums)
        # if nums_sorted[-1] < 0:
        #     return nums_sorted[-1]
        # for i in range(len(nums)):
        #     sum += nums[i]
        #     res = max(sum, res)
        #     if sum < 0:
        #         sum = 0
        # return res
        n = len(nums)
        if n == 1: return nums[0]
        if n == 2: return max(nums[0], nums[1], nums[0] + nums[1])
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(dp[0] + nums[1], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        return max(dp)