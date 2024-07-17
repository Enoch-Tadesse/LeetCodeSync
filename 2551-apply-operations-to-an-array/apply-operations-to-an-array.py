class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i]*=2
                nums[i+1] = 0
        ptr = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[i] , nums[ptr] = nums[ptr] , nums[i]
                ptr+=1
        return nums
        