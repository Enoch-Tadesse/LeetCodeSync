class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        closest_sum = float('inf')
        nums.sort()
        for i in range(len(nums)-2):
            j = i + 1
            k = len(nums)-1
            while j < k:
                curr_sum = nums[i] + nums[j] + nums[k]
                if target == curr_sum:
                    return curr_sum
                if abs(curr_sum - target) < abs(closest_sum - target):
                    closest_sum = curr_sum
                if curr_sum > target:
                    k-=1
                else:
                    j+=1
        return closest_sum
                
