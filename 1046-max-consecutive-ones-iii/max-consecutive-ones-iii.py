class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ans = 0
        used = 0
        l = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                used += 1
            while used > k:
                used -= nums[l] == 0
                l += 1
            ans = max(r- l+ 1, ans)
        return ans