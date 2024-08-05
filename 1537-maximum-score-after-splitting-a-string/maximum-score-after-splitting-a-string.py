class Solution:
    def maxScore(self, s: str) -> int:
        zeroCount = s.count('0')
        m = len(s)
        total = 0
        left = 0
        right = zeroCount
        for l in range(len(s)-1):
            if s[l] == "0":
                left += 1
                right -= 1
            total = max(total, left + (m - l - 1 - right))
        return total