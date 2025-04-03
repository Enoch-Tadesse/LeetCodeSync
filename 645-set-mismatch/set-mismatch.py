class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dup = -1
        for i in range(len(nums)):
            x = abs(nums[i])
            if nums[x-1] < 0:
                dup = x
            else:
                nums[x-1] *= -1
        for i in range(len(nums)):
            if nums[i] > 0:
                return [dup, i + 1]