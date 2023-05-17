var climbStairs = function(n) {
    if(n < 2) return n;
    let dp = new Array(n).fill(0);
    dp[0] = 1, dp[1] = 2;
    for(let i = 2; i < n; i++){
        dp[i] = dp[i - 1] + dp[i - 2];
    }
    return dp[n - 1]
};