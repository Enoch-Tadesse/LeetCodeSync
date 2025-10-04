class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        dp = [set() for _ in range(n)]
        dp[0].add(0)
        for i in range(n):
            for j in range(i + 1, n):
                diff = stones[j] - stones[i]
                found = False
                for ele in [diff - 1, diff, diff + 1]:
                    if ele in dp[i]:
                        found = True
                        dp[j].add(diff)
        return len(dp[-1]) > 0