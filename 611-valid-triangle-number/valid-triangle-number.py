class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # if a , b , and c, a + b > c
        nums.sort()
        counter = 0
        for i in range(len(nums)-2):
            for j in range(i + 1, len(nums) - 1):
                a , b = nums[i], nums[j]
                counter += max(0, bisect_left(nums, a + b) - (j + 1))
        return counter