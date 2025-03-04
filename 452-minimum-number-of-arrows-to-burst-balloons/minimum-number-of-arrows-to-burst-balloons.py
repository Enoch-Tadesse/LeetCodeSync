class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        last = points[0][1]
        counter = 1
        for i in range(1, len(points)):
            if points[i][0] <= last:
                last = min(points[i][1], last)
            else:
                counter += 1
                last = points[i][1]
        return counter
        