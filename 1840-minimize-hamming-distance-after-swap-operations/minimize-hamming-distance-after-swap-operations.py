class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        par = {i : i for i in range(n)}

        def find(x):
            if par[x] != x:
                par[x] = find(par[x])
            return par[x]
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                par[py] = px
        
        for a, b in allowedSwaps:
            union(a, b)
        group = defaultdict(list)
        for i in range(n):
            group[find(i)].append(i)
        cnt = 0
        for k, v in group.items():
            idx = v
            s = Counter([source[i] for i in idx])

            for ele in [target[i] for i in idx]:
                if s[ele] > 0:
                    s[ele] -= 1
                else:
                    cnt += 1

        return cnt
