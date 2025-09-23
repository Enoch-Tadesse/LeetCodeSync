class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        MOD = 10 ** 9 + 7
        # get the matrix to be profit by group
        m = minProfit
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = 1
        for (p, g) in zip(profit, group):
            for i in range(m, -1, -1):
                for j in range(n, g - 1, -1):
                    candx, candy = max(0, i - p) , j - g
                    dp[i][j] = (dp[candx][candy] + dp[i][j]) % MOD
        
        return sum(dp[m]) % MOD