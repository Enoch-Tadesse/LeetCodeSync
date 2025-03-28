class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        dom = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == dom:
                count += 1
            else:
                count -= 1
            if count == 0:
                dom = nums[i]
                count = 1
        return dom