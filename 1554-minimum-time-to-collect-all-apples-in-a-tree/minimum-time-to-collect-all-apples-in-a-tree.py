class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = defaultdict(list)
        for u , v in edges:
            adj[u].append(v)
            adj[v].append(u)
        if n == 1:
            return 0
        def dfs(head, par):
            if len(adj[head]) == 0:
                return hasApple[head] * 2
            ans = 0
            for nei in adj[head]:
                if nei == par:
                    continue
                ans += dfs(nei, head)
            if head == 0:
                return ans
            if ans != 0:
                return ans + 2
            elif hasApple[head]:
                return 2
            return 0
        return dfs(0, -1)
