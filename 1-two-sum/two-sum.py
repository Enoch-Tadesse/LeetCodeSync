class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index_list = []
        for i in range(len(nums)):
            it = i+1
            for j in range(it, len(nums), 1):
                if nums[i] + nums[j] == target:
                    index_list.append(i)
                    index_list.append(j)
                    return index_list

        