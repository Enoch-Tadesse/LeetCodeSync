class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        curr_sum = sum(nums[:k])
        max_sum = curr_sum
        for i in range(0, len(nums)-k):
            curr_sum -= nums[i]
            curr_sum += nums[i + k]
            max_sum = max(max_sum, curr_sum)
        return float(max_sum) / k

        