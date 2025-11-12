class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        nums = [int(a == "T") for a in answerKey]
        nums2 = [num ^ 1 for num in nums]
        return max(self.solve(nums, k), self.solve(nums2, k))

    def solve(self, nums, k):
        ans = 0
        l = 0
        used = 0
        for r in range(len(nums)):
            while nums[r] == 0 and used == k:
                used -= nums[l] == 0
                l += 1
            if nums[r] == 0:
                used += 1
            ans = max(ans, r - l + 1)
        return ans