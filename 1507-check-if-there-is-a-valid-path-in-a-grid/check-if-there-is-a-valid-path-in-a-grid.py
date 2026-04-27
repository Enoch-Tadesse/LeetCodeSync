class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        self.moves = {
            1 : [(0,-1), (0,1)],
            2 : [(-1, 0), (1, 0)],
            3 : [(0, -1), (1, 0)],
            4 : [(0, 1), (1, 0)],
            5 : [(0, -1), (-1, 0)],
            6 : [(-1, 0), (0, 1)]
        }
        seen = set()
        seen.add((0,0))
        if self.traverse(grid, 0, 0, seen):
            return True
        return False
    def traverse(self, grid, r, c, seen):
        if r == len(grid) - 1 and c == len(grid[0]) - 1:
            return True
        for op in self.moves[grid[r][c]]:
            dr, dc = op
            nr, nc = dr + r , dc + c
            if (nr, nc) in seen:
                continue
            if not self.isValid(grid, nr, nc):
                continue
            ir , ic = -1 * dr, -1 * dc
            if (ir, ic) not in self.moves[grid[nr][nc]]:
                continue
            seen.add((nr, nc))
            if self.traverse(grid, nr, nc, seen):
                return True
            seen.discard((nr,nc))
        return False

    def isValid(self, grid, r, c):
        return (0 <= r < len(grid) and 0 <= c < len(grid[0]))