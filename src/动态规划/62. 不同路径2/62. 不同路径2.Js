/**
 * @param {number[][]} obstacleGrid
 * @return {number}
 */
var uniquePathsWithObstacles = function(obstacleGrid) {
    // dp五部曲
    // 1. 明确dp数组和下标含义
    // 2. 确定递推公式
    // 2. 初始化dp数组
    // 3. 确定遍历顺序
    // 4. 举例验证
    const m = obstacleGrid.length; n = obstacleGrid[0].length;
    let dp = Array(m).fill(0).map(() => Array(n).fill(0));
    for(let i = 0; i < m && obstacleGrid[i][0] == 0; i++){
        dp[i][0] = 1
    };
    for(let j = 0; j < n && obstacleGrid[0][j] == 0; j++){
        dp[0][j] = 1
    };
    for(let i = 1; i < m; i++){
        for(let j = 1; j < n; j++){
            if(obstacleGrid[i][j] === 0){
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
            };    
        }
    };
    return dp[m-1][n-1]
};