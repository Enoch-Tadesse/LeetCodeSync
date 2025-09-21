class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        curr = sum([i * num for i, num in enumerate(nums)])
        total = sum(nums)
        ans = curr
        n = len(nums)
        for i in range(len(nums) -1, -1, -1):
            curr = curr + total - nums[i] * (n)
            ans = max(curr, ans)
        return ans
