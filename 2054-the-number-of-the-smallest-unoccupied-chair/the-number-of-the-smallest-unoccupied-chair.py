class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        starter, ender = times[targetFriend][0], times[targetFriend][1]
        times.sort()
        avail = [i for i in range(len(times))]
        occupied = [] # (endTime, chair)
        time = 0
        idx = 0
        while True:
            while occupied and occupied[0][0] <= time:
                e, c = heappop(occupied)
                heappush(avail, c)
            s , e = times[idx]
            if s == time:
                x = heappop(avail)
                heappush(occupied, (e, x))
                if s == starter and e == ender:
                    return x
                idx += 1
            time += 1
            