# 思路：
"""
确定dp数组（dp table）以及下标的含义
确定递推公式
dp数组如何初始化
确定遍历顺序
举例推导dp数组
"""

# dp[i]表示到第i个楼梯的总花费
# dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
# dp[0], dp[1] = 0, 0
# 从前向后

def minCostClimbingStairs(cost):
    cost.append(0)
    dp = [0] * (len(cost))
    dp[0], dp[1] = 0, 0
    if len(cost) < 3: return 0
    for i in range(2, len(cost)):
        dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
    return dp[len(cost) - 1]



cost = [10, 15, 20]
# cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print(minCostClimbingStairs(cost))