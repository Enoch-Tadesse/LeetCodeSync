class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        res = 0
        rank = {i : 0 for i in range(1, n + 1)}
        par = {i : i for i in range(1, n + 1)}

        def find(a):
            if par[a] != a:
                par[a] = find(par[a])
            return par[a]

        def union(a, b):
            if find(a) == find(b):
                return False
            ra, rb = find(a), find(b)
            if rank[ra] > rank[rb]:
                par[rb] = ra
            elif rank[rb] > rank[ra]:
                par[ra] = rb
            else:
                par[ra] = rb
                rank[rb] += 1
            return True

        for i, (a , b) in enumerate(edges):
            if not union(a, b):
                ans = i
        return edges[ans]