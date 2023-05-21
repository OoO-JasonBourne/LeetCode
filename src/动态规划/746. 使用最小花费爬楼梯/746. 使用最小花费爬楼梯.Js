var minCostClimbingStairs = function(cost) {
    // 确定dp数组（dp table）以及下标的含义
    // 确定递推公式
    // dp数组如何初始化
    // 确定遍历顺序
    // 举例推导dp数组
    if(cost.length < 2) return 0
    cost.push(0);
    dp = new Array(cost.length).fill(0);
    dp[0] = 0, dp[1] = 0;
    for(let i = 2; i < cost.length; i++){
        dp[i] = Math.min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2]);
    }
    return dp[cost.length - 1]
};