class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] <= 0:
                nums[i] = float("inf")
        for i in range(len(nums)):
            if nums[i] == float("-inf") or abs(nums[i]) > len(nums):
                continue
            if nums[abs(nums[i]) - 1] > 0:
                nums[abs(nums[i]) - 1] *= -1
        for i in range(len(nums)):
            if nums[i] >= 0:
                return i + 1
        return len(nums) + 1