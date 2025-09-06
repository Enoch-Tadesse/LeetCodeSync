class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        n = len(pairs)
        dp = [1] * n
        pairs.sort()
        for i in range(n):
            a, b = pairs[i]
            for j in range(i + 1, n):
                c , d = pairs[j]
                if b < c:
                    dp[j] = max(dp[j] , dp[i] + 1)
        return max(dp)