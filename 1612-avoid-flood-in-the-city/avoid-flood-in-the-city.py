class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        # of all that are occupied, which one is worth saving
        n = len(rains)
        seen = set()
        nxt_rain = defaultdict(deque)
        ans = [-1] * n
        for r in range(n):
            nxt_rain[rains[r]].append(r)
        for ele in nxt_rain:
            nxt_rain[ele].popleft()
        h = [] # (idx)
        l = 0
        for r in range(n):
            if rains[r] > 0 and rains[r] in seen:
                return []
            if rains[r] != 0:
                seen.add(rains[r])
                # put the next one here
                if len(nxt_rain[rains[r]]) > 0:
                    heappush(h, nxt_rain[rains[r]].popleft())
                continue
            while h and h[0] <= r:
                heappop(h)
            if not h:
                ans[r] = 1
                continue
            ans[r] = rains[heappop(h)]
            seen.discard(ans[r])
        return ans
            
