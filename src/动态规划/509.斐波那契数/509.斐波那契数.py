def fb(n):
    """
    动态规划五部曲：
    1. 确定dp数组（dp table）以及下标的含义
    dp[i]表示第i个斐波那契数值为dp[i]
    2. 确定递推公式
    dp[i] = dp[i-1] + dp[i-2]
    3. dp数组如何初始化
    dp[0] = 0
    dp[1] = 1
    4. 确定遍历顺序
    从前往后
    5. 举例推导dp数组
    [0, 1, 1, 2, 3, 5, 8, 13, 21...]
    """
    if n < 2:
        return n
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-2] + dp[i-1]
    return dp[i]

print(fb(8))
