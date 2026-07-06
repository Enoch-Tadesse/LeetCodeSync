class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        cnt = 0
        intervals.sort(key = lambda x : (x[0], -x[1]))
        l, r = intervals[0][0], intervals[0][1]
        for i in range(1, len(intervals)):
            nl, nr = intervals[i]
            if r < nl:
                l, r = nl, nr
            else:
                if r >= nr: cnt += 1
                r = max(r, nr)
        return len(intervals) - cnt