class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: 
        [-1,1,1,2,3]
        """
        count = 0
        for i in range(len(nums)):
            for j in range(len(nums)-1, i, -1):
                sum = nums[i] + nums[j]
                if sum >= target:
                    continue
                else:
                    count+=1
        return count