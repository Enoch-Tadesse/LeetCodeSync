class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        MOD = 10 ** 9 + 7
        # get the matrix to be profit by group
        m = sum(profit)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = 1
        for (p, g) in zip(profit, group):
            if g > n:
                continue
            for i in range(m, p -1, -1):
                for j in range(n, g - 1, -1):
                    candx, candy = i - p , j - g
                    dp[i][j] = (dp[candx][candy] + dp[i][j]) % MOD
        counter = 0
        for i in range(minProfit, len(dp)):
            for j in range(len(dp[0])):
                counter = (counter + dp[i][j]) % MOD
        return counter