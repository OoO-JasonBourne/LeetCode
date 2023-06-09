def uniquePaths(m, n):
    """
    确定dp数组（dp table）以及下标的含义
    确定递推公式
    dp数组如何初始化
    确定遍历顺序
    举例推导dp数组
    """
    dp = [[0] * (n) for _ in range(m)]
    for i in range(m):
        dp[i][0] = 1
    for j in range(n):
        dp[0][j] = 1

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[m - 1, n - 1]

# 简洁写法
def uniquePaths(self, m: int, n: int) -> int:
    dp = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[-1][-1]
