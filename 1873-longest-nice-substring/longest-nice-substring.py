class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        self.res = ""
        self.cnt = float("-inf")
        self.helper(s)
        return self.res
        
    def helper(self, s):
        if len(s) <= 1:
            return
        lett = set(s)
        for i in range(len(s)):
            if s[i].swapcase() not in lett:
                self.helper(s[:i])
                self.helper(s[i+1:])
                return
        if self.cnt < len(s):
            self.res = s
            self.cnt = max(self.cnt, len(s))
        return
