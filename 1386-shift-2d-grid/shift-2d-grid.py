class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        ans = [[0] * cols for _ in range(rows)]

        # div for row, mod for col
        for r in range(rows):
            for c in range(cols):
                place = r * cols + c + k
                nc, nr = place % cols, (place // cols) % rows
                ans[nr][nc] = grid[r][c]
        return ans                