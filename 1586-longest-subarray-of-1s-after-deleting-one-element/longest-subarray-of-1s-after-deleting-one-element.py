class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        fk = -1
        isFk = False
        ans = 0
        l = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                if isFk:
                    l = fk + 1
                    fk = r
                else:
                    fk = r
                    isFk = True
            ans = max(ans, r - l)
        return ans