class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        coll = set()
        result = 0
        i = 0
        j = 0
        while j < len(s):
            while s[j] in coll: 
                coll.remove(s[i])
                i+=1
            coll.add(s[j])
            j+=1
            result = max(result, j-i)
        return result