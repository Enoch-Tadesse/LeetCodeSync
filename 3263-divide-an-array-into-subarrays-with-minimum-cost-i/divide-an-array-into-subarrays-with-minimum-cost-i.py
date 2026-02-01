class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        first = second = third = float("inf")
        first = nums[0]
        for i in range(len(nums)):
            if i == 0:
                continue
            num = nums[i]
            if num <= second:
                third = second
                second = num
            elif num < third:
                third = num
        return first + second + third