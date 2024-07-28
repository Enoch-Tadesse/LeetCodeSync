class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s
        max_num = 1
        max_str = s[0]

        for i in range(0 , len(s)-1):
            for j in range(i+1 , len(s)):
                if j - i + 1 > max_num and s[i:j+1] == s[i:j+1][::-1]:
                    max_num = j-i+1
                    max_str = s[i:j+1]
        return max_str