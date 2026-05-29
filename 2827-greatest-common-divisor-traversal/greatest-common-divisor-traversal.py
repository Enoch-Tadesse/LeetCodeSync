class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        
        fac = defaultdict(set)
        def factor(num, idx):
            i = 2
            while i * i <= num:
                if num % i != 0:
                    i += 1
                    continue
                while num % i == 0:
                    num //= i
                fac[i].add(idx)
                i += 1
            if num > 1:
                fac[num].add(idx)
        for  i in range(len(nums)):
            factor(nums[i], i)
        print(fac)
        par = {i : i for i in range(len(nums))}
        def find(x):
            if x != par[x]:
                par[x] = find(par[x])
            return par[x]
        def union(x, y):
            px, py = find(x), find(y)
            par[px] = py
        for v in fac.values():
            v = list(v)
            for i in range(1, len(v)):
                union(v[i], v[i - 1])
        ans = find(0)
        for i in range(1, len(nums)):
            if ans != find(i):
                return False
        return True