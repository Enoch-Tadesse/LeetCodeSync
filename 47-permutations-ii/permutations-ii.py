class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.counts = defaultdict(int)
        for num in nums:
            self.counts[num] += 1
        self.ans = []
        self.backtrack(list(), nums, self.counts)
        self.ans.sort()
        output = [[]]
        for ans in self.ans:
            if ans != output[-1]:
                output.append(ans)
        return output[1:]
    def backtrack(self, temp, nums, counts):
        if len(temp) == len(nums):
            # if temp not in self.ans:
            self.ans.append(temp[:])
            return
        
        for num in nums:
            if counts[num] == 0:
                continue
            counts[num] -= 1
            temp.append(num)
            self.backtrack(temp, nums, counts)
            temp.pop()
            counts[num] += 1