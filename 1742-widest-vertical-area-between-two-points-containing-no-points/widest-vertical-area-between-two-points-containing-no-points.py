class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort(key = lambda x : x[0])
        max_width = 0
        for i in range(len(points)-1, 0, -1):
            if points[i][0] - points[i-1][0] > max_width:
                max_width = points[i][0] - points[i-1][0]
        return max_width
        