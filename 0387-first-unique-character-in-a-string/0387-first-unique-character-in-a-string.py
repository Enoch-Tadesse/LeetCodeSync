class Solution:
    def firstUniqChar(self, s: str) -> int:
        span = Counter(s)
        for i in range(len(s)):
            if span[s[i]] == 1:
                return i
        return -1