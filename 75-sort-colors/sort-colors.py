class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1,-1,-1):
            largest = nums[i]
            for j in range(i-1 , -1, -1):
                if nums[j] > nums[i]:
                    nums[j] , nums[i] = nums[i] , nums[j]
        


        