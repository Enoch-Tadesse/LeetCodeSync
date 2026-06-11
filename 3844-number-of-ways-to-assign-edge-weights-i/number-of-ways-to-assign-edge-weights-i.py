class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        n = len(edges)
        vis = set([1])
        
        def dfs(node):
            if not node:
                return 0
            depth = 0
            for nei in adj[node]:
                if nei in vis: continue
                vis.add(nei)
                depth = max(depth, dfs(nei) + 1)
            return depth

        return pow(2, dfs(1) - 1, 10 ** 9 + 7)