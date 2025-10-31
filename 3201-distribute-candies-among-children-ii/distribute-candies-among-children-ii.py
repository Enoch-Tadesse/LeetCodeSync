class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        if n < limit:
            limit = n
        def calculate(left):
            _max = min(limit, left)
            _min = left - _max
            return _max - _min + 1
        ans = 0
        for i in range(max(0, n - 2 * limit), n + 1):
            if i > limit:
                break
            left = n - i
            ans += calculate(left)
        return ans