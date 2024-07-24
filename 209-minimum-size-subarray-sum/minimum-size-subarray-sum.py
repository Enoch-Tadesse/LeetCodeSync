class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        result = float('inf')
        r = 0
        l = 0
        sum = 0
        while r < len(nums):
            sum += nums[r]
            while sum >= target:
                result = min(result, r - l + 1)
                sum -= nums[l]
                l+=1
            r+=1
        return 0 if result == float('inf') else result