class Solution:
    def trailingZeroes(self, n: int) -> int:
        def helper(n , x):
            if x > n:
                return 0
            return n // x + helper(n , x * 5)
        return helper(n , 5)