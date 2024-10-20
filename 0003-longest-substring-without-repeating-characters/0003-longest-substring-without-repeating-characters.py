class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        longest = 0
        l = 0
        for r in range(len(s)):
            if s[r] in chars:
                while s[r] in chars:
                    chars.remove(s[l])
                    l+=1
            longest = max(longest , r-l+1)    
            chars.add(s[r])
        return longest

                    