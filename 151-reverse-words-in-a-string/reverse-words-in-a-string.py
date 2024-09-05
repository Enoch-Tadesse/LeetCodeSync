class Solution:
    def reverseWords(self, s: str) -> str:
        l = 0
        res = []
        for r in range(len(s)):
            while l < len(s) and s[l] == " ":
                l+=1
            r = l
            while r < len(s) and s[r] != " ":
                r+=1
            if r - l == 0:
                break
            res.append(s[l:r])
            r+=1
            l = r
        res.reverse()
        return (" ").join(res)
