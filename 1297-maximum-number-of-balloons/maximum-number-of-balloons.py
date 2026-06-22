class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        factor = {
            'b' : 1,
            'a' : 1,
            'l' : 2,
            'o' : 2,
            'n' : 1
        }
        ans = float("inf")
        cnt = Counter(text)
        bad = False
        for c in factor:
            if c not in cnt:
                bad = True
                break
        if bad:
            return 0
        for c in cnt:
            if c not in factor: continue
            ans = min(ans, cnt[c] // factor[c])
        return ans