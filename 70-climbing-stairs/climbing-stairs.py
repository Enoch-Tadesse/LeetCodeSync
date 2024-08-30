class Solution:
    def climbStairs(self, n: int) -> int:
        self.memo = defaultdict()
        def helper(n ,k):
            if self.memo.get(k,None):
                return self.memo[k]
            if k == n:
                return 1
            if k > n:
                return 0
            self.memo[k] = helper(n, k+1) + helper(n, k+2)
            return self.memo[k]
        return helper(n, 0)