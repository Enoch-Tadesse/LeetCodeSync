class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        i = 0
        while i <= len(haystack)-len(needle):
            if haystack[i:i+len(needle)] == needle:
                return i
            i+=1
        return -1