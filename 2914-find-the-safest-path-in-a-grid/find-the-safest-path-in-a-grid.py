class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        # start bfs over all the thiefs and for every cell, get the closest manhatan distance
        rows, cols = len(grid), len(grid[0])
        dist = [[float("inf")] * cols for _ in range(rows)]
        q = deque()
        vis = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    q.append((r, c))
                    vis.add((r, c))
        level = 0
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                dist[r][c] = level
                for dr, dc in dirs:
                    nr, nc = dr + r, dc + c
                    if not(0 <= nr < rows and 0 <= nc < cols):
                        continue
                    if (nr, nc) in vis:
                        continue
                    q.append((nr, nc))
                    vis.add((nr, nc))
            level += 1
        if grid[0][0] == 1 or grid[rows - 1][cols - 1] == 1:
            return 0


        heap = [(-dist[0][0], 0, 0)]
        vis = set()
        while heap:
            d, r, c = heappop(heap)
            d *= -1
            if r == rows - 1 and c == cols - 1:
                return d
            vis.add((r, c))
            for dr, dc in dirs:
                nr, nc = dr + r, dc + c
                if not(0 <= nr < rows and 0 <= nc < cols):
                    continue
                if (nr, nc) in vis:
                    continue
                vis.add((nr, nc))
                heappush(heap, (-min(d, dist[nr][nc]), nr, nc))
        return 0
