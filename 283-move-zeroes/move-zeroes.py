class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        w = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[r] , nums[w] = nums[w] , nums[r]
                w += 1
        return nums