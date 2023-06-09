/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
// var uniquePaths = function(m, n) {
//     // 初始化dp数组
//     let dp = Array(m).fill(0).map(() => Array(n).fill(0));
//     for(let i = 0; i < m; i++){
//         dp[i][0] = 1
//     };
//     for(let j = 0; j < n; j++){
//         dp[0][j] = 1
//     };

//     for(let i = 1; i < m; i++){
//         for(let j = 1; j < n; j++){
//             dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
//         }
//     }

//     return dp[m-1][n-1]
// };

// 简洁写法
const uniquePaths = (m, n) => {
    const dp = Array(m).fill(1);
    
    for (let i = 1; i < n; i++) {
      for (let j = 1; j < m; j++) {
        dp[j] += dp[j - 1];
      }
    }
    
    return dp[m - 1];
  };
  