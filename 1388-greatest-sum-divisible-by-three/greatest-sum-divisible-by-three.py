class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        nums = [(num % 3, num) for num in nums]
        dp = [0, float("-inf"), float("-inf")]
        for r, n in nums:
            new = [0, 0, 0]
            if r == 0:
                new[0] = dp[0] + n
                new[1] = dp[1] + n
                new[2] = dp[2] + n
            elif r == 1:
                new[0] = max(dp[0], dp[2] + n)
                new[1] = max(dp[1] , dp[0] + n)
                new[2] = max(dp[2], dp[1] + n)
            else:
                new[0] = max(dp[0], dp[1] + n)
                new[1] = max(dp[1], dp[2] + n)
                new[2] = max(dp[2], dp[0] + n)
            dp = new
        return dp[0]
