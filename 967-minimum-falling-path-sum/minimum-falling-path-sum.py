class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows , cols = len(matrix) , len(matrix[0])
        if rows == 1:
            return min(matrix[0])
        dp = [[float("inf")] * cols for _ in range(rows)]
        dirs = [(1, 0), (1, -1), (1, 1)]
        for r in range(rows):
            for c in range(cols):
                if r == 0:
                    dp[r][c] = matrix[r][c]
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if not (0 <= nr < rows) or not(0 <= nc < cols):
                        continue
                    dp[nr][nc] = min(dp[nr][nc], matrix[nr][nc] + dp[r][c])
        return min(dp[-1])  
                
