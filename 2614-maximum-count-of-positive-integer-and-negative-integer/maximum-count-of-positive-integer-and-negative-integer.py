class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pos = 0
        neg = 0
        for num in nums:
            if num < 0:
                neg+=1
            elif num > 0:
                pos+=1
        return max(pos,neg)