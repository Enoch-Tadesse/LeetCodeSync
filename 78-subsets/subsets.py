class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.back([], 0, nums)
        return self.ans

    def back(self,temp, start, nums):
        self.ans.append(temp[:])
        for i in range(start, len(nums)):
            temp.append(nums[i])
            self.back(temp, i + 1, nums)
            temp.pop()