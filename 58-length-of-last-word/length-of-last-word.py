class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.rstrip()
        length = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] != " ":
                length+=1
            else:
                break        
        return length
