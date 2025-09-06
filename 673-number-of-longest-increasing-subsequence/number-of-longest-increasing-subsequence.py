class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        ways = [1] * n
        for i in range(n):
            for j in range(i+1, n):
                if nums[j] > nums[i]:
                    if dp[i] + 1 > dp[j]:
                        ways[j] = ways[i]
                        dp[j] = dp[i] + 1
                    elif dp[i] + 1 == dp[j]:
                        ways[j] += ways[i]
        _m = max(dp)
        return sum(c for l, c in zip(dp, ways) if l == _m)