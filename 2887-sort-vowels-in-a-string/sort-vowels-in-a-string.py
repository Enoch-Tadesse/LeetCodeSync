class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        t = ""
        vowels = []
        vowels_list = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
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
            if isVowel(s[i]):
                t+=(vowels[j])
                j+=1
            else:
                t+=(s[i])
        return t
        