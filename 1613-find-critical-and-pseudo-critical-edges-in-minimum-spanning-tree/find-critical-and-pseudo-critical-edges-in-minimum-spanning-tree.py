class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        self.edges = [edge + [i] for i, edge in enumerate(edges)]
        self.edges.sort(key = lambda x : x[2])
        _min = self.mst(n, self.edges)
        pseudo = []
        critical = []
        for i , e in enumerate(self.edges):
            temp = [x for j, x in enumerate(self.edges) if j != i]
            if self.mst(n, temp) > _min:
                critical.append(e[3])
            elif self.mst(n, self.edges, force=i) == _min:
                pseudo.append(e[3])
        return [critical, pseudo]


    def mst(self, n, edges, force=None):
        par = {i:i for i in range(n)}
        rank = {i : 0 for i in range(n)}

        def find(node):
            if node != par[node]:
                par[node] = find(par[node])
            return par[node]

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return False
            if rank[rx] < rank[ry]:
                par[rx] = ry
            elif rank[rx] > rank[ry]:
                par[ry] = rx
            else:
                par[rx] = ry
                rank[ry] += 1
            return True
        counter = 0
        if force is not None:
            u, v, w, _ = self.edges[force]
            counter += w
            union(u, v)
        for x, y, w, _ in edges:
            if force is not None and (x, y, w) == (edges[force][0],edges[force][1],edges[force][2]):
                continue
            if union(x, y):
                counter += w
        roots = set(find(i) for i in range(n))

        return counter if len(roots) == 1 else float("inf")