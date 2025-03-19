class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counter = 0
        left = 0
        for right in range(2, len(nums)):
            if nums[left] == 0:
                nums[left] = not nums[left]
                nums[left + 1] = not nums[left + 1]
                nums[left + 2] = not nums[left + 2]
                counter += 1
            left += 1
        if nums[-1] == 0 or nums[-2] == 0:
            return -1
        return counter