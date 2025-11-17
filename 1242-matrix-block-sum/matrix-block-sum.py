class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
        
        for r in range(rows):
            for c in range(cols):
                prefix[r+1][c+1] = mat[r][c] + prefix[r][c+1] + prefix[r+1][c] - prefix[r][c]
        
        ans = [[0] * cols for _ in range(rows)]
        
        for r in range(rows):
            for c in range(cols):
                r1 = max(0, r - k)
                c1 = max(0, c - k)
                r2 = min(rows - 1, r + k)
                c2 = min(cols - 1, c + k)
                
                ans[r][c] = (
                    prefix[r2+1][c2+1]
                    - prefix[r1][c2+1]
                    - prefix[r2+1][c1]
                    + prefix[r1][c1]
                )
        return ans
