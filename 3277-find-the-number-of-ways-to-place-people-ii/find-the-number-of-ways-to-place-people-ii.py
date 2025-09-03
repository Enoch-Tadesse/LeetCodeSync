class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[0], -x[1]))
        n = len(points)
        counter = 0
        for i in range(n - 1):
            _, y = points[i]
            _min = float("-inf")
            for j in range(i + 1, n):
                _, y1 = points[j]
                if y < y1:
                    continue
                elif _min <= y1 <= y:
                    counter += 1
                    _min = y1 + 1
        return counter
