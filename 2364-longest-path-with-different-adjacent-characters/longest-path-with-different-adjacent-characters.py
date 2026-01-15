class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        ans = 1

        adj = defaultdict(list)
        for i in range(len(parent)):
            adj[parent[i]].append(i)

        def dfs(curr):
            nonlocal ans
            cand = []
            ret = 0
            for nei in adj[curr]:
                x = dfs(nei)
                if s[nei] != s[curr]:
                    ret = max(ret, x)
                    cand.append(x)
            cand.sort(reverse=True)
            if len(cand) == 1:
                ans = max(ans, cand[0] + 1)
            elif len(cand) >= 2:
                ans = max(ans, cand[0] + cand[1] + 1)
            return ret + 1
        dfs(0)
        return ans
