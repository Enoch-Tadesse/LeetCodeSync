class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]
        temp = nums[0]
        for i in range(1,len(nums)):
            temp = max(temp+nums[i], nums[i])
            result = max(result, temp)
        return result
