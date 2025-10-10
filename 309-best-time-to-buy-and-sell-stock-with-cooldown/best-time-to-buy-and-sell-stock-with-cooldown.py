class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * n for _ in range(2)]
        dp[1][0] = -prices[0]
        # 1 means hold, zero means gone
        for i in range(1, n):
            dp[0][i] = max(dp[0][i-1], dp[1][i-1] + prices[i])
            dp[1][i] = max(dp[1][i-1], (dp[0][i-2] if i - 2 >= 0 else 0) - prices[i])
        return dp[0][n-1]
        