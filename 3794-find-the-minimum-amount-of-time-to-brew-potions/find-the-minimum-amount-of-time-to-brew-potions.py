class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n = len(skill)
        dp = [0] * n
        m = len(mana)
        acc = 0
        for i in range(m):
            cand = 0
            new = []
            for j in range(n):
                takes = mana[i] * skill[j]
                if j > 0:
                    new.append(takes + new[-1])
                else:
                    new.append(takes)
            for k in range(1,n):
                cand = max(cand, dp[k] - new[k-1])
            cand = max(cand, dp[0])
            acc += cand
            dp = new
        return acc + dp[-1]