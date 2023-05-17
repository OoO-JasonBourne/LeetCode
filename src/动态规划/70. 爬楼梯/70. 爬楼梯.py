def climbStairs(n):
    # 滚动数组
    if n < 2: return n
    p, q, r = 1, 2, 0
    for i in range(3, n + 1):
        r = q + p
        p = q
        q = r
    return r

    """
    动态规划五部曲:
    1. 确定dp数组（dp table）以及下标的含义
    2. 确定递推公式
    3. dp数组如何初始化
    4. 确定遍历顺序
    5. 举例推导dp数组
 
 
    if n < 2: return n
    dp = [0] * n
    dp[0] = 1
    dp[1] = 2
    for i in range(2, n):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n - 1]
    """

n = 5
print(climbStairs(n))


