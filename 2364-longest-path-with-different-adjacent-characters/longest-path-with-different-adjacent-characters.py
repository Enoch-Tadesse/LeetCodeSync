class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        ans = 1

        adj = defaultdict(list)
        for i in range(len(parent)):
            adj[parent[i]].append(i)

        def dfs(curr):
            nonlocal ans
            ret = 0
            a, b = float("-inf"), float("-inf")
            for nei in adj[curr]:
                x = dfs(nei)
                if s[nei] != s[curr]:
                    ret = max(ret, x)
                    if x >= a:
                        a, b = x , a
                    elif x >= b:
                        b = x
            a = max(a, 0)
            b = max(b, 0)
            
            ans = max(ans, a + b + 1)
            return ret + 1
        dfs(0)
        return ans
