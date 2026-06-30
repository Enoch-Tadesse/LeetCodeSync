class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ans = 0
        k = 3
        l = 0
        cnt = defaultdict(int)
        for r in range(len(s)):
            cnt[s[r]] += 1
            while len(cnt) == k:
                ans += len(s) - r
                cnt[s[l]] -= 1
                if cnt[s[l]] == 0:
                    del cnt[s[l]]
                l += 1
        return ans