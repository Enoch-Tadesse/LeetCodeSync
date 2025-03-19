class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.counts = defaultdict(int)
        for i in range(len(nums)):
            nums[i] = str(nums[i])
        for num in nums:
            self.counts[num] += 1
        self.ans = []
        self.checker = set()
        self.backtrack(list(), nums, self.counts)
        return self.ans
    def backtrack(self, temp, nums, counts):
        if len(temp) == len(nums):
            check = "".join(temp)
            if check not in self.checker:
                res = [int(a) for a in temp]
                self.ans.append(res)
                self.checker.add(check)
            return
        
        for num in nums:
            if counts[num] == 0:
                continue
            counts[num] -= 1
            temp.append(num)
            self.backtrack(temp, nums, counts)
            temp.pop()
            counts[num] += 1