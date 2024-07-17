class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_idx = {}
        for idx, num in enumerate(nums):
            target2 = target - num
            if target2 in num_idx:
                return [num_idx[target2], idx]
            else:
                num_idx[num] = idx
        print(num_idx)

        