class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        nums = set(coins)
        @cache
        def dp(curr):
            if curr == 0:
                return 0
            if curr in nums:
                return 1
            ans = float("inf")
            for num in nums:
                if curr - num >= 0:
                    cand = dp(curr - num)
                    cand2 = 1
                    ans = min(ans, cand + cand2)
            return ans
        ans = dp(amount)
        return -1 if ans == float("inf") else ans