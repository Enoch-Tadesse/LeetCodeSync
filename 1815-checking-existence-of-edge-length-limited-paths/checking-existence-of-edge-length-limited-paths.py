class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        parent = {i : i for i in range(n)}
        def find(a):
            if parent[a] != a:
                parent[a] = find(parent[a])
            return parent[a]
        def union(a, b):
            ua , ub = find(a) , find(b)
            parent[ua] = ub
        qs = defaultdict(list)
        for index, (a , b , limit) in enumerate(queries):
            qs[limit].append((a, b, index))
        adj = defaultdict(list)
        ans = [None] * len(queries)
        for a, b , w in edgeList:
            adj[w].append((a, b))
        for x in sorted(set(list(qs.keys()) + list(adj.keys()))):
            for u, v, idx in qs[x]:
                ans[idx] = find(u) == find(v)
            for u , v in adj[x]:
                union(u, v)
        return ans