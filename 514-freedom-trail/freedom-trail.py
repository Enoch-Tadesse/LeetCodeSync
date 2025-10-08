class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        self.index = defaultdict(list)
        self.length = len(ring)
        for i , c in enumerate(ring):
            self.index[c].append(i)
        self.ans = float("inf")
        return self.dfs(0, key, 0)
    @cache
    def dfs(self, curr, key, start):
        if start == len(key):
            # self.ans = min(self.ans, cost)
            return 0
        cand = float("inf")
        for ind in self.index[key[start]]:
            step1 = abs(curr - ind)
            cost1 = self.dfs(ind, key, start + 1)  + step1 + 1
            step2 = self.length - step1
            cost2 = self.dfs(ind, key, start + 1)  + step2 + 1
            cand = min(cand, cost1, cost2)
        return cand
        