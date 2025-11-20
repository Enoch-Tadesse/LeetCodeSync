class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        intervals.sort()
        ans = []
        curr_left, curr_right = intervals[0][0], intervals[0][1]
        for l , r in intervals:
            if l <= curr_right:
                curr_right = max(r, curr_right)
            else:
                ans.append([curr_left, curr_right])
                curr_left , curr_right = l , r
        ans.append([curr_left, curr_right])
        return ans