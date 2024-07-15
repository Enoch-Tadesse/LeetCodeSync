class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums_count = []
        def count(key,nums):
            count = 0
            for num in nums:
                if num < key:
                    count+=1
            return count
        for num in nums:
            nums_count.append(count(num, nums))
        return nums_count