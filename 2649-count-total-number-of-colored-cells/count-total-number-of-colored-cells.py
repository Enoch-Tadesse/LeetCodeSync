class Solution:
    def coloredCells(self, n: int) -> int:
        curr = [1,0]
        for i in range(1, n):
            temp = curr[0] + 4 + curr[1]
            curr[1] += 4
            curr[0] = temp
        return curr[0]