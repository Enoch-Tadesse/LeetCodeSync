class Solution:
    def numSquares(self, n: int) -> int:
        nums = [i * i for i in range(1, int(n ** 0.5) + 1)]
        dp = [float("inf")] * (n + 1)
        dp[0] = 0
        for i in range(len(nums)):
            for j in range(nums[i], len(dp)):
                dp[j] = min(dp[j] , dp[j - nums[i]] + 1)
        return dp[n]