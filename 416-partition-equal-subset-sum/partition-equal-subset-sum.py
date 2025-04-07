class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums.sort(reverse=True)
        self.nums = nums
        total = sum(nums)
        if total & 1:
            return False
        half = total // 2
        # look for this half
        return self.recur(half, 0, 0)
    @cache
    def recur(self, target, start, curr):
        if curr > target:
            return False
        if curr == target:
            return True
        for i in range(start, len(self.nums)):
            if self.recur(target, i + 1, curr + self.nums[i]):
                return True
        return False
        