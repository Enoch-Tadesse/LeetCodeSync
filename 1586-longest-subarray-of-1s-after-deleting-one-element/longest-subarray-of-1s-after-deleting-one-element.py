class Solution(object):
    def longestSubarray(self, nums):
        try:
             r = nums.index(0) + 1
        except:
             return len(nums) - 1
        l = 0
        result = r-1
        while r < len(nums):
            temp = r 
            while r<len(nums) and nums[r] != 0:
                r+=1
            result = max(result, r-l-1)
            l = temp
            r+=1
        return result



        