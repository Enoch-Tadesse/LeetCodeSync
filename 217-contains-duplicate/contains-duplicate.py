class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_map = {}
        for num in nums:
            if num in nums_map:
                return True
            else:
                nums_map[num] = " "
        return False