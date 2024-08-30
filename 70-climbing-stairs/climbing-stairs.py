class Solution:
    def climbStairs(self, n: int) -> int:
        @lru_cache
        def helper(n ,k):
            if k == n:
                return 1
            if k > n:
                return 0
            return helper(n, k+1) + helper(n, k+2)
        return helper(n, 0)