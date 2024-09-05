class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ""
        left = len(word1)
        right = len(word2)
        l = 0
        r = 0
        leftTurn = True
        while l < left and r < right:
            if leftTurn:
                output+=word1[l]
                l+=1
            else:
                output += word2[r]
                r+=1
            leftTurn = False if leftTurn else True
        if l < left:
            output += word1[l:]
        if r < right:
            output += word2[r:]
        return output