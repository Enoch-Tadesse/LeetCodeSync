class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        neg = self.negBin(nums)
        pos = self.posBin(nums)
        return max(neg , len(nums) - pos)
    def negBin(self, nums):
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (r + l) // 2
            if nums[mid] >= 0:
                r = mid - 1
            elif nums[mid] < 0:
                l = mid + 1
        return l
    def posBin(self, nums):
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (r + l) // 2
            if nums[mid] > 0:
                r = mid - 1
            elif nums[mid] <= 0:
                l = mid + 1
        return l

