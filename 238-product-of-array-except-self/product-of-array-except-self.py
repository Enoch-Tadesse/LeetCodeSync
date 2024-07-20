class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = [1] * len(nums)
        pre = 1
        post = 1
        for i in range(len(nums)):
            output[i] = pre
            pre*=nums[i]
        for j in range(len(nums)-1,-1,-1):
            output[j] = post * output[j]
            post*=nums[j]
        return output
        