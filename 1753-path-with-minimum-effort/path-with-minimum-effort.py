class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        h = [(0, 0, 0)]
        rows, cols = len(heights) , len(heights[0])
        ans = float("-inf")
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = set()
        while h:
            hei, row, col = heappop(h)
            ans = max(ans, hei)
            if row == rows - 1 and col == cols - 1:
                return ans
            if (row, col) in visited:
                continue
            visited.add((row, col))
            for dr, dc in dirs:
                nr , nc = row + dr , col + dc
                if not(0 <= nr < rows) or not(0 <= nc < cols):
                    continue
                diff = abs(heights[row][col] - heights[nr][nc])
                heappush(h, (diff, nr, nc))