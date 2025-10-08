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
            return 0
        cand = float("inf")
        for ind in self.index[key[start]]:
            cost = self.dfs(ind, key, start + 1)
            step1 = abs(curr - ind)
            step2 = (self.length - abs(curr - ind))
            cand = min(cand, step1 + cost + 1, step2 + cost + 1)
        return cand
        