class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        first = abs(x - z)
        second = abs(y - z)
        if first > second:
            return 2
        elif second > first:
            return 1
        else:
            return 0