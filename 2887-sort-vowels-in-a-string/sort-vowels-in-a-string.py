class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        t = ""
        vowels = []
        vowels_list = "aeiouAEIOU"
        def isVowel(char):
            if char in vowels_list:
                return True
            return False
        for string in s:
            if isVowel(string):
                vowels.append(string)
        vowels.sort()
        j = 0
        for i in range(len(s)):
            if s[i] in vowels_list:
                t+=(vowels[j])
                j+=1
            else:
                t+=(s[i])
        return t
        