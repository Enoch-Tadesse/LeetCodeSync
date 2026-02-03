class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        ans = []

        tin = {}
        timer = [0]
        low = {}
        visited = set()

        adj = defaultdict(list)
        for a, b in connections:
            adj[a].append(b)
            adj[b].append(a)
        
        def dfs(curr, prev):
            tin[curr] = low[curr] = timer[0]
            timer[0] += 1
            visited.add(curr)

            for nei in adj[curr]:
                if nei == prev:
                    continue
                if nei in visited:
                    low[curr] = min(low[nei], low[curr])
                else:
                    dfs(nei, curr)
                    low[curr] = min(low[nei], low[curr])
                    if low[nei] > tin[curr]:
                        ans.append([nei, curr])
        for i in range(n):
            if i not in visited:
                dfs(i, -1)
        return ans

