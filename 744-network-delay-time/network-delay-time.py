class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float("inf")] * (n + 1)
        dist[0] = 0
        dist[k] = 0
        adj = defaultdict(list)
        for u , v , w in times:
            adj[u].append((v, w))
        h = [(0, k)]
        while h:
            d , key = heappop(h)
            for nei , wei in adj[key]:
                if dist[key] + wei < dist[nei]:
                    dist[nei] = dist[key] + wei
                    heappush(h, (dist[nei], nei))
        ans = max(dist)
        return -1 if ans == float("inf") else ans