class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        temp = set()
        l = r = 0
        output = 0
        while r < len(s):
            while s[r] in temp:
                temp.remove(s[l])
                l+=1
            temp.add(s[r])
            r+=1
            output = max(r-l, output)
        return output