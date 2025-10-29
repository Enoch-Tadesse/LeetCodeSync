class Solution:
    def secondMinimum(self, n, edges, time, change):
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        heap = [(0, 1)]
        times = [[] for _ in range(n + 1)]

        while heap:
            wei, curr = heappop(heap)
            
            if len(times[curr]) < 2 and (len(times[curr]) == 0 or times[curr][-1] != wei):
                times[curr].append(wei)
            else:
                continue

            if len(times[n]) == 2:
                return times[n][1]

            for nei in adj[curr]:
                if len(times[nei]) >= 2:
                    continue
                sign = wei // change
                nxt = 0
                if sign & 1:
                    nxt = time + (sign + 1) * change
                else:
                    nxt = wei + time
                heappush(heap, (nxt, nei))
