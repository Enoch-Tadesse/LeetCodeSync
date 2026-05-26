class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        cnt = set()
        ans = set()
        for w in word:
            if w.swapcase() in cnt:
                ans.add(w.lower())
            cnt.add(w)
        return len(ans)