class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        l , r = 0, 0
        adj = defaultdict(list)
        for u, v, c in edges:
            if not(online[u] and online[v]): continue
            adj[u].append((v, c))
            r = max(c , r)
        n = len(online)

        def can(wei):
            dist = [float("inf")] * n
            dist[0] = 0

            heap = [(0, 0)]

            while heap:
                total, node = heappop(heap)
                if total != dist[node]:
                    continue
                if node == n - 1:
                    return total <= k
                for nei, c in adj[node]:
                    if c < wei:
                        continue
                    ntotal = total + c
                    if ntotal < dist[nei] and ntotal <= k:
                        dist[nei] = ntotal
                        heappush(heap, (ntotal, nei))

            return False

        while l <= r:
            mid = l + (r - l) // 2
            if can(mid):
                l = mid + 1
            else:
                r = mid - 1
        return r
