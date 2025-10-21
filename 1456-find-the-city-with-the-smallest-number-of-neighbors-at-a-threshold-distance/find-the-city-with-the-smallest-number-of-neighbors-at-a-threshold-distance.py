class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj = defaultdict(list)
        for u , v , w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        def traverse(curr, k):
            heap = [(0, curr)]
            counts = 0
            visited = set()
            while heap:
                wei, ele = heappop(heap)
                if ele in visited:
                    continue
                visited.add(ele)
                counts += 1
                for e, w in adj[ele]:
                    if wei + w <= k:
                        heappush(heap, (wei + w, e))
            return counts - 1
            
        ans, _min = 0, float("inf")
        for c in range(n):
            cand = traverse(c, distanceThreshold)
            if cand <= _min:
                ans = c
                _min = cand
        return ans