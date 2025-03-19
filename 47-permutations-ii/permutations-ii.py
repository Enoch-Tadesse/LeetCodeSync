class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.counts = defaultdict(int)
        for num in nums:
            self.counts[num] += 1
        nums.sort()
        self.ans = []
        self.backtrack(list(), nums, self.counts)
        return self.ans
    def backtrack(self, temp, nums, counts):
        if len(temp) == len(nums):
            if temp not in self.ans:
                self.ans.append(temp[:])
            return
        
        for i in range(len(nums)):
            if counts[nums[i]] == 0 or (i > 0 and nums[i-1] == nums[i]):
                continue
            counts[nums[i]] -= 1
            temp.append(nums[i])
            self.backtrack(temp, nums, counts)
            temp.pop()
            counts[nums[i]] += 1