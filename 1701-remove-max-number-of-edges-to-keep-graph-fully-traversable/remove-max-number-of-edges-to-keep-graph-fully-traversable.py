class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        # 1 is alice, 2 is bob and 3 is both
        # always use both connection without creating a loop
        # using the previous data, try to use the alice and bob, make it connected
        # take the spare from the three
        def find(x, par):
            if par[x] != x:
                par[x] = find(par[x], par)
            return par[x]
        def union(x, y, par):
            px, py = find(x, par), find(y, par)
            if px == py:
                return True
            par[px] = py
            return False
        
        def ind(edges, ref):
            spare = 0
            for a, b , _ in edges:
                spare += union(a, b , ref)
            p = find(1, ref)
            for i in range(2, n + 1):
                if p != find(i, ref):
                    return [False, 0]
            return [True, spare]

        types = [[] for _ in range(4)]
        for e, a, b in edges:
            types[e].append((a, b , e))
        par = {i : i for i in range(1, n + 1)}
        
        spare = 0
        for a, b , e in types[3]:
            spare += union(a, b, par)
        
        d, s = ind(types[2], deepcopy(par))
        if not d:
            return -1
        spare += s
        d, s = ind(types[1], deepcopy(par))
        if not d:
            return -1
        return spare + s
        
        
            