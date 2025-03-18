class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        used = 0
        l = 0
        ans = 0
        for r in range(len(nums)):
            while used & nums[r]:
                used^= nums[l]
                l += 1
            used |= nums[r]
            ans = max(ans, r - l + 1)
        return ans