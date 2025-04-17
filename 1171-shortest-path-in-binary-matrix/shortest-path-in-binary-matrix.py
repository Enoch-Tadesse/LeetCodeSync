class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        seen = [[0] * len(grid[0]) for _ in range(len(grid))]
        if grid[0][0] != 0:
            return -1
        if len(grid) == 1:
            return 1
        q = deque([(0,0)])
        depth = 0
        while q:
            depth += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                for nr in range(max(0, r-1), min(len(grid), r + 2)):
                    for nc in range(max(0, c-1), min(len(grid[0]), c + 2)):
                        if nr == r and nc == c:
                            continue
                        if seen[nr][nc] == 1 or grid[nr][nc] == 1:
                            continue
                        if nr == len(grid) - 1 and nc == len(grid[0]) - 1:
                            return depth + 1
                        q.append((nr, nc))
                        seen[nr][nc] = 1
        return -1
                        