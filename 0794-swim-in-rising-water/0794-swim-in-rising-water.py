class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        heap = [(grid[0][0], 0, 0)]
        ans = 0
        rows , cols = len(grid) , len(grid[0])
        visited = set()
        while heap:
            val, cr, cc = heappop(heap)
            visited.add((cr, cc))
            ans = max(val, ans)
            if cr == rows - 1 and cc == cols - 1:
                return ans
            dirs = [(1, 0), (0, 1), (-1, 0), (0 , -1)]
            for dr, dc in dirs:
                nr , nc = cr + dr , cc + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    heappush(heap, (grid[nr][nc], nr, nc))
        return ans