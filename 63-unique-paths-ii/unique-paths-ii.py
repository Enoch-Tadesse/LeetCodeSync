class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        grid = obstacleGrid
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return 0
        rows, cols = len(grid) , len(grid[0])
        dp = [[0] * (cols) for _ in range(rows)]
        dp[0][0] = 1
        dirs = [(0, -1), (-1, 0)]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    continue
                for dr, dc in dirs:
                    nr = r + dr
                    nc = c + dc
                    if not(0 <= nr < rows and 0 <= nc < cols):
                        continue
                    dp[r][c] += dp[nr][nc] 
        return dp[-1][-1]