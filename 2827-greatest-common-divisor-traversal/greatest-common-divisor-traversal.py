_max = 10 ** 5 + 7
pre = [0] * _max
for i in range(2, _max):
    if pre[i] == 0:
        for j in range(i, _max, i):
            if pre[j] == 0:
                pre[j] = i


class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        
        fac = defaultdict(set)
        par = {i : i for i in range(len(nums))}
        def find(x):
            if x != par[x]:
                par[x] = find(par[x])
            return par[x]
        def union(x, y):
            px, py = find(x), find(y)
            par[px] = py

        def factor(x, i):
            while x != 1:
                fac[pre[x]].add(i)
                x //= pre[x]

        for  i in range(len(nums)):
            factor(nums[i], i)
        
        for v in fac.values():
            v = list(v)
            for i in range(1, len(v)):
                union(v[i], v[i - 1])
        ans = find(0)
        for i in range(1, len(nums)):
            if ans != find(i):
                return False
        return True