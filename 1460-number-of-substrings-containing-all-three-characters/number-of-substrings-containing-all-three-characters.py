class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        cnt = defaultdict(int)

        def valid():
            return cnt['a'] > 0 and cnt['b'] > 0 and cnt['c'] > 0
        
        ans = 0

        l = 0
        for r in range(len(s)):
            cnt[s[r]] += 1
            while valid():
                ans += len(s) - r
                cnt[s[l]] -= 1
                l += 1
        return ans