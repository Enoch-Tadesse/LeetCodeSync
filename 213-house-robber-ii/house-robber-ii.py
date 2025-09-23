class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return sum(nums)
        ans = 0
        for i in range(len(nums)):
            t, nt = 0 , 0
            for j in range(i + 1, len(nums) + i):
                j = j % len(nums)
                t, nt = max(t, nt + nums[j]), t
            ans = max(ans, t, nt)
            if i > 1:
                break
        return ans
        