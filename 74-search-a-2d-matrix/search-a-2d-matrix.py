class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l , r = 0 , len(matrix) * len(matrix[0]) - 1
        while l <= r:
            mid = l + (r - l) // 2
            row = mid // len(matrix[0])
            col = mid % len(matrix[0])
            cand = matrix[row][col]
            if cand == target:
                return True
            elif cand < target:
                l = mid + 1
            else:
                r = mid - 1
        return False