class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        conns = []
        n = len(points)
        for i in range(n):
            x1, y1 = points[i][0], points[i][1]
            for j in range(i + 1, n):
                x2, y2 = points[j][0], points[j][1]
                dist = abs(x1 - x2) + abs(y1 - y2)
                conns.append((dist, i , j))
        conns.sort()
        par = {i : i for i in range(n)}
        rank = {i : 0 for i in range(n)}

        def find(x):
            if x != par[x]:
                par[x] = find(par[x])
            return par[x]
        
        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return False
            if rank[rx] < rank[ry]:
                par[rx] = ry
            elif rank[ry] < rank[rx]:
                par[ry] = rx
            else:
                par[rx] = ry
                rank[ry] += 1
            return True
        
        counter = 0
        for w, x, y in conns:
            if union(x, y):
                counter += w
        return counter