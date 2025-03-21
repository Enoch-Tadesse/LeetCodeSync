class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.seen = set()
        self.temp = []
        self.ans = []
        self.helper(nums)
        return self.ans
    def helper(self, nums):
        if len(self.temp) == len(nums):
            self.ans.append(self.temp[:])
            return
        for num in nums:
            if num not in self.seen:
                self.temp.append(num)
                self.seen.add(num)
                self.helper(nums)
                self.seen.discard(num)
                self.temp.pop()