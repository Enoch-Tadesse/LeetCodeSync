class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = [1] * len(nums)
        pre = 1
        post = 1
        for i in range(1,len(nums)):
            output[i] = pre * nums[i-1]
            pre*=nums[i-1]
        for j in range(len(nums)-1,-1,-1):
            output[j] = post * output[j]
            post*=nums[j]
        return output
        