class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return sum(nums)
        ans = 0
        for i in range(len(nums)):
            t, nt = 0 , 0
            new = nums[i+1:] + nums[:i]
            for j in range(len(new)):
                t, nt = max(t, nt + new[j]), t
            ans = max(ans, t, nt)
        return ans
        