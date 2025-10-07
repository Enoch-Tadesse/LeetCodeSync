class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        counter = 0
        rows , cols = len(grid) , len(grid[0])
        start, end, total = None, None, 0
        for r in range(rows):
            for c in range(cols):
                total += grid[r][c] == 0
                if grid[r][c] == 1:
                    start = (r, c)
                if grid[r][c] == 2:
                    end = (r, c)

        visited = set([(start[0], start[1])])
        def back(r, c):
            nonlocal counter
            if grid[r][c] == 2:
                counter += len(visited) == total + 2
                return

            dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
            for dr, dc in dirs:
                nr , nc = dr + r , dc + c
                if (nr, nc) in visited:
                    continue
                if not(0 <= nr < rows) or not(0 <= nc < cols):
                    continue
                if grid[nr][nc] == -1:
                    continue

                visited.add((nr, nc))
                back(nr, nc)
                visited.discard((nr, nc))
        back(start[0], start[1])
        return counter