class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        leftSum = 0
        total = sum(nums)
        for i in range(len(nums)):
            if total - leftSum - nums[i] == leftSum:
                return i
            leftSum+=nums[i]
        return -1