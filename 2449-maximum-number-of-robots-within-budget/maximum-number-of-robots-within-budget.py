class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        # sum(runningCosts) can be done with sliding window
        # max(chargeTimes) can be tracked with mono queue

        ans = 0
        q = deque([])
        l = 0
        n = len(runningCosts)
        curr = 0
        for r in range(n):
            while q and chargeTimes[q[-1]] <= chargeTimes[r]:
                q.pop()
            q.append(r)

            curr += runningCosts[r]

            while q and chargeTimes[q[0]] + (r - l + 1) * curr > budget:
                curr -= runningCosts[l]
                if q[0] <= l:
                    q.popleft()
                l += 1

            ans = max(ans, r - l + 1)
        return ans
