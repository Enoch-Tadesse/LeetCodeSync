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
        zeros = []
        for num in nums:
            if num == 0:
                zeros.append(num)
            else:
                result.append(num)
        result.extend(zeros)
        return result
        