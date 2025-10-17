class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        notEquals = []
        par = {chr(i + ord('a')) : chr(i + ord('a')) for i in range(26)}
        rank = {chr(i + ord('a')) : 0 for i in range(26)}
        def find(x):
            if par[x] != x:
                par[x] = find(par[x])
            return par[x]

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return
            if rank[rx] > rank[ry]:
                par[ry] = rx
            elif rank[rx] < rank[ry]:
                par[rx] = ry
            else:
                par[ry] = rx
                rank[rx] += 1
            return

        for eq in equations:
            if "!" in eq:
                notEquals.append((eq[0], eq[-1]))
            else:
                union(eq[0], eq[-1])
        for a , b in notEquals:
            if find(a) == find(b):
                return False
        return True
