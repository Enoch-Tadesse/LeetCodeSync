class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        cnt = 0
        intervals.sort(key = lambda x : (x[0], -x[1]))
        r = intervals[0][1]
        for i in range(1, len(intervals)):
            _, nr = intervals[i]
            if r >= nr: cnt += 1
            r = max(r, nr)
        return len(intervals) - cnt