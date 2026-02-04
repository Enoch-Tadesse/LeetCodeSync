class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        n = len(s)
        size = int(n ** 0.5) + 1
        groups = [[] for _ in range(size)]

        for i, enum in enumerate(queries):
            l, r, k = enum
            groups[l // size].append((l, r, k, i))
        
        ans = 0
        q = len(queries)
        output = [False] * q
        L, R = 0, -1

        cnts = defaultdict(int)
        def add(index):
            nonlocal ans
            ele = s[index]
            cnts[ele] += 1
            if cnts[ele] & 1: ans += 1
            else: ans -= 1
        def remove(index):
            nonlocal ans
            ele = s[index]
            cnts[ele] -= 1
            if cnts[ele] & 1: ans += 1
            else: ans -= 1


        for g in groups:
            if len(g) == 0:
                continue
            g.sort(key=lambda x : (x[1], x[0]))

            for l , r, k, i in g:
                while R < r:
                    R += 1
                    add(R)
                while R > r:
                    remove(R)
                    R -= 1
                while L < l:
                    remove(L)
                    L += 1
                while L > l:
                    L -= 1
                    add(L)
                length = r - l + 1
                to = 0
                if length & 1 == 0:
                    to = ans // 2
                else:
                    to = (ans - 1) // 2
                output[i] = (to <= k)
        return output