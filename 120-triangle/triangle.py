class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        @cache
        def dp(row, index):
            if row == len(triangle):
                return 0
            right = float("inf")
            if index < len(triangle[row]):
                right = dp(row + 1, index + 1)
            left = dp(row + 1, index)
            return min(right, left) + triangle[row][index]
        return dp(0, 0)