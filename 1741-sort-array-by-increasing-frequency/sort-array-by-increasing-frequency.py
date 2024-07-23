class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        fre = {}
        for num in nums:
            if num not in fre:
                fre[num] = 1
            else: fre[num] += 1
        return sorted(nums, key = lambda x : (fre[x], -x))
        
        
        