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
                    ans = min(dp(curr - num) + 1, ans)
            return ans
        ans = dp(amount)
        return -1 if ans == float("inf") else ans