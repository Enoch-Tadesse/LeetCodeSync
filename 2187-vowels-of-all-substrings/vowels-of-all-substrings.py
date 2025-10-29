class Solution:
    def countVowels(self, word: str) -> int:
        total = 0
        n = len(word)
        for i, w in enumerate(word):
            if w in 'aeiou':
                total += (n - i) * (i + 1)
        return total