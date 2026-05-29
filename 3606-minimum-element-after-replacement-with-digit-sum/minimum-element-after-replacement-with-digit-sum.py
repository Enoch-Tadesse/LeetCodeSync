class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans = float("inf")

        def sum(num):
            g = 0
            while num > 0:
                g += num % 10
                num //= 10
            return g
        for num in nums:
            ans = min(ans, sum(num))
        return ans