class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # num, amm
        n = len(nums)
        dp = [1] * n
        for i in range(1,n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i],dp[j]+1)
        return max(dp)