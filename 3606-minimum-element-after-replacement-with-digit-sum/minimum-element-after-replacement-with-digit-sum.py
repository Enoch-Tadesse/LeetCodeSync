class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans = float("inf")

        def sum(num):
            g = 0
            for n in str(num):
                g += int(n)
            return g
        for num in nums:
            ans = min(ans, sum(num))
        return ans