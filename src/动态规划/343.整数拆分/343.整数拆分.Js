var integerBreak = function (n) {
    const dp = Array(n + 1).fill(0);
    dp[2] = 1; dp[3] = 2;
    for (let i = 2; i <= n; i++) {
        for (let j = 1; j < parseInt(n / 2 + 1); j++){
            dp[i] = Math.max(dp[i], j * Math.max((i - j), dp[i - j]))
        }
    }
    return dp[n]
};

console.log(integerBreak(2))