class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        par = {i : i for i in range(n)}
        def find(x):
            if par[x] != x:
                par[x] = find(par[x])
            return par[x]
        def union(x, y):
            px, py = find(x), find(y)
            par[px] = py
        l = 0
        for r in range(n):
            while nums[r] - nums[l] > maxDiff:
                l += 1
            union(r, l)
        ans = []
        for a, b in queries:
            ans.append(find(a) == find(b))
        return ans
                