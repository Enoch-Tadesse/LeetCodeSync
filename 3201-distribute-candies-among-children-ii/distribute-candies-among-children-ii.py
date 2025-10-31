class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        ans = 0
        for i in range(max(0, n - 2 * limit), min(limit + 1, n + 1)):
            ans += 2 * min(limit, n - i) - (n - i) + 1
        return ans