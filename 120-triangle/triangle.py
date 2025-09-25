class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                cand = float("inf")
                dir = [-1, 0]
                for d in dir:
                    if 0 <= j + d < len(triangle[i-1]):
                        cand = min(cand, triangle[i-1][j + d])
                triangle[i][j] += cand
        return min(triangle[-1])