class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split(" ")
        counter = 0
        forbid = set(brokenLetters)
        for word in words:
            for w in word:
                if w in forbid:
                    break
            else:
                counter += 1
        return counter