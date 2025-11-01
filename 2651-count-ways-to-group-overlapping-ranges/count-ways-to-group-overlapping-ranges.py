class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        ranges.sort(key = lambda x : (x[0], -x[1]))
        groups = 0
        r = ranges[0][1]
        for i in range(1, len(ranges)):
            if ranges[i][0] <= r:
                r = max(ranges[i][1], r)
            else:
                groups += 1
                r = ranges[i][1]

        groups += 1

        return pow(2, groups, 10 ** 9 + 7)