class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.res = 0
        self.back(nums, 0, 0)
        return self.res

    def back(self, nums, start, temp):
        self.res += temp
        for i in range(start, len(nums)):
            self.back(nums, i + 1, temp ^ nums[i]) 