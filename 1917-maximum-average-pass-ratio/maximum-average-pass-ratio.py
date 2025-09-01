class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        h = []
        for p , t in classes:
            d = (p + 1) / (t + 1) - p / t
            heappush(h , (-d, p , t))
        while extraStudents:
            _ , p , t = heappop(h)
            p , t = p + 1, t + 1
            d = (p + 1) / (t + 1) - p / t
            heappush(h , (-d, p , t))
            extraStudents -= 1
        total = sum(p / t for _ , p , t in h)
        return total / len(classes)
        