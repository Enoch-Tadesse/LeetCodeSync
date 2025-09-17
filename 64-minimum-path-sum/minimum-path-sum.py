class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows , cols = len(grid) , len(grid[0])
        dp = [[0] * cols for _ in range(rows)]
        dirs = [(0, -1), (-1, 0)]
        for r in range(rows):
            for c in range(cols):
                cand = []
                for dr, dc in dirs:
                    nr , nc = r + dr, c + dc
                    if not(0 <= nr < rows and 0 <= nc < cols):
                        continue
                    cand.append(dp[nr][nc])
                dp[r][c] += grid[r][c]
                if cand:
                    dp[r][c] += min(cand)
        return dp[-1][-1]