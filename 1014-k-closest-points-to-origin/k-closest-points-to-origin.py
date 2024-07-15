class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        points.sort(key=lambda item: (item[0] ** 2 + item[1] ** 2))
        return points[:k]