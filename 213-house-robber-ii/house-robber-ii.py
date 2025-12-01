class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return sum(nums)
        ans = 0
        for i in range(len(nums)):
            r, nr = 0 , 0
            for j in range(i + 1, len(nums) + i):
                j = j % len(nums)
                num = nums[j]
                r, nr = nr + num, max(r, nr)
            ans = max(ans, r, nr)
        return ans
