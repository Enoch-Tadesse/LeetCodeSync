class MedianFinder:

    def __init__(self):
        self.counts = 0
        self._max = []
        self._min = []

    def addNum(self, num: int) -> None:
        if self._max and num > -1 * self._max[0]:
            heappush(self._min, num)
        else:
            heappush(self._max, -num)
        while len(self._max) > len(self._min) + 1:
            heappush(self._min, -1 * heappop(self._max))
        while len(self._min) > len(self._max) + 1:
            heappush(self._max, -1 * heappop(self._min))

    def findMedian(self) -> float:
        if (len(self._max) == len(self._min)):
            return (-1 * self._max[0] + self._min[0]) / 2
        elif len(self._max) > len(self._min):
            return -1 * self._max[0]
        return self._min[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()