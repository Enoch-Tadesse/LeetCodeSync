class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        # self.res = ""
        # self.cnt = float("-inf")
        ans = self.helper(s)
        return ans
        
    def helper(self, s):
        if len(s) <= 1:
            return ("")
        lett = set(s)
        for i in range(len(s)):
            if s[i].swapcase() not in lett:
                l = self.helper(s[:i])
                r = self.helper(s[i+1:])
                return (max(l , r , key=lambda x : len(x)))
        return s

        # if self.cnt < len(s):
        #     self.res = s
        #     self.cnt = max(self.cnt, len(s))
        # return
