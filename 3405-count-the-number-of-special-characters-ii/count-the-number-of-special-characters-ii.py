class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        ogcnt = [0] * 26
        for w in word:
            if w.islower():
                ogcnt[ord(w) - ord('a')] += 1
        curr = [0] * 26
        ans = 0

        for w in word:
            if w.isupper():
                idx = ord(w.lower()) - ord('a')
                if ogcnt[idx] and curr[idx] == ogcnt[idx]:
                    ans += 1
                curr[idx] -= 1
            else:
                curr[ord(w) - ord('a')] += 1
        return ans