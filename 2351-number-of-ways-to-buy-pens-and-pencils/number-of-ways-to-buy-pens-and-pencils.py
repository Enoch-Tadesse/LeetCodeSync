class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        dp = [0] * (total + 1)
        dp[0] = 1
        
        for i in range(cost1, total + 1):
            dp[i] += dp[i - cost1]
        
        for i in range(cost2, total + 1):
            dp[i] += dp[i - cost2]
        
        return sum(dp)
