class Solution:
    def rob(self, nums: List[int]) -> int:
        nt, t = 0 , 0
        for num in nums:
            nt, t = t, max(t, nt + num)
        return max(nt, t)