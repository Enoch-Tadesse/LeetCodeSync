class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        # 2 3 4 4 5 6
        nums.sort()
        ans = 0
        l , r = 0 , len(nums) - 1
        while l < r:
            ans = max(ans, nums[l] + nums[r])
            l += 1
            r -= 1
        return ans