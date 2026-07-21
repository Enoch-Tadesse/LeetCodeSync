class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        cand = []
        l = 0
        for r in range(len(s)):
            if s[r] == s[l]:
                continue
            fac = -1 if s[l] == "1" else 1
            cand.append((fac * (r - l), l, r - 1))
            l = r
        fac = -1 if s[l] == "1" else 1
        cand.append((fac * (len(s) - l), l, len(s) - 1))

        pre = [0]
        for i in range(len(s)):
            pre.append(pre[-1] + (s[i] == "1"))

        ans = 0
        for i in range(1, len(cand) - 1):
            val, l, r = cand[i]
            if val >= 0:
                continue
            curr = -1 * cand[i][0] + (cand[i - 1][0] + cand[i + 1][0])
            curr += pre[cand[i-1][1]]
            curr += pre[-1] - pre[cand[i + 1][2] + 1]
            ans = max(ans, curr)

        if ans == 0:
            ans = s.count("1")
        return ans