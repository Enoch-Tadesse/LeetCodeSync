class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = 0
        result = float('inf')
        temp = 0
        while r < len(nums):
            temp += nums[r]
            while temp >= target:
                temp -= nums[l]
                result = min(result, r-l+1)
                l+=1
            r+=1
        return result if result != float('inf') else 0