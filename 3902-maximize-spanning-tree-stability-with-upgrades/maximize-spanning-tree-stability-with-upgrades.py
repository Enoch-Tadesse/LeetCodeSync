class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        ans = float("inf")
        later = []
        par = {i : i for i in range(n)}
        def find(x):
            if par[x] != x:
                par[x] = find(par[x])
            return par[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False
            par[px] = py
            return True

        man = 0

        for u, v, s, m in edges:
            if not m:
                later.append((u, v, s))
            else:
                ans = min(ans, s)
                if not union(u, v):
                    return -1
                man += 1
        later.sort(key=lambda x : -x[-1])

        cand = []
        for u, v, s in later:
            if union(u, v):
                cand.append(s)
        if man + len(cand) != n - 1:
            return -1
        cand.sort()
        for i in range(min(k, len(cand))):
            cand[i] *= 2
        if cand:
            ans = min(ans, min(cand))
        return ans