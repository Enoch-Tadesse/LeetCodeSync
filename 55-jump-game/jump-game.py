class Solution:
    def canJump(self, nums: List[int]) -> bool:
        fur = 0

        for i in range(len(nums)):
            if fur < i:
                return False
            fur = max(fur, i + nums[i])
        return True