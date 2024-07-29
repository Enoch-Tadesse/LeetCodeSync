class Solution(object):
    def longestSubarray(self, nums):
        l , r = 0 , 0
        for i in range(len(nums)):
            r+=1
            if nums[i] == 0:
                break
        else: return len(nums)-1
        result = r-l-1
        while r < len(nums):
            temp = r
            while r<len(nums) and nums[r] != 0:
                r+=1
            result = max(result, r-l-1)
            l = temp
            r+=1
        return result


        