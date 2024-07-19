class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: 
        [-1,-1,1,1,2,3]
        """
        nums.sort()
        count = 0
        i , j = 0 , len(nums) - 1
        while i < j:
            if nums[i] + nums[j] < target:
                count+=(j-i)
                i += 1
            else:
                j-=1
        return count