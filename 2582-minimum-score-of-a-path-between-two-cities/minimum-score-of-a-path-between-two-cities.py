class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        par = {i : i for i in range(1, n + 1)}
        _min = {i : float("inf") for i in range(1, n + 1)}
        def find(x):
            if par[x] != x:
                par[x] = find(par[x])
            return par[x]
        def union(x, y, d):
            px, py = find(x), find(y)
            par[px] = py
            _min[py] = min(_min[py], _min[px], d)

        for a, b, d in roads:
            union(a, b, d)
        return _min[find(1)]
        