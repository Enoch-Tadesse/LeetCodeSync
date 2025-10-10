class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # at each point it is buy or sell
        n = len(prices)
        dp = [[0] * n for _ in range(2)]
        # 0 means the buy
        # 1 means the sold
        dp[1][0] = -(prices[0] + fee)
        for i in range(1, n):
            dp[0][i] = max(dp[0][i-1], dp[1][i-1] + prices[i]) # keep non bought or sell it
            dp[1][i] = max(dp[1][i-1], dp[0][i-1] - fee - prices[i]) # keep last sold, or sell it here, rn
        return dp[0][n-1]