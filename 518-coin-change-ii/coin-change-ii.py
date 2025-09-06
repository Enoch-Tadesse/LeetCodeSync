sys.setrecursionlimit(10000)
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1 
        for c in coins:
            for ele in range(c , amount + 1):
                dp[ele] += dp[ele - c]
        return dp[amount]
 