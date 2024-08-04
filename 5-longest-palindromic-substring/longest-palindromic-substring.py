class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        resLen = 0
        for k in range(len(s)):
            l = k
            r = k
            while r < len(s) and l >= 0 and s[r] == s[l]:
                if r - l + 1 > resLen:
                    result = s[l:r+1]
                    resLen = max(resLen, r-l+1)
                l-=1
                r+=1
            
            l = k
            r = k + 1
            while r < len(s) and l >= 0 and s[r] == s[l]:
                if r - l + 1 > resLen:
                    result = s[l:r+1]
                    resLen = max(resLen, r-l+1)
                l-=1
                r+=1
            
        return result