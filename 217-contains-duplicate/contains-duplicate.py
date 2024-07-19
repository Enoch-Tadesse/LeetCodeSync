class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums2 = set(nums)
        if len(nums) > len(nums2):
            return True
        return False