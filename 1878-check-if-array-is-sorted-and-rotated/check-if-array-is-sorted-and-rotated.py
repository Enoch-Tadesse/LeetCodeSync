class Solution:
    def check(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            curr = nums[i:] + nums[:i]
            if curr == sorted(curr):
                return True
        return False