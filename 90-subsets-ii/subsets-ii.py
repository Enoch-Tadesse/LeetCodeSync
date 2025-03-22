class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.ans = []
        self.temp = []
        self.back(0 , nums)
        return self.ans

    def back(self, start, nums):
        self.ans.append(self.temp[:])
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue
            self.temp.append(nums[i])
            self.back(i + 1, nums)
            self.temp.pop()
