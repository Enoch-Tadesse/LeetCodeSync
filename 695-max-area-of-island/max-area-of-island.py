class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        _max = 0
        self.visited = set()
        self.dirs = [(-1, 0) , (1, 0), (0, -1) , (0 , 1)]
        self.grid = grid
        self.seen = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r , c) not in self.visited:
                    self.visited.add((r,c))
                    self.seen = 1
                    self.traverse(r, c, len(grid), len(grid[0]))
                    _max = max(_max, self.seen)
        return _max

    def traverse(self, nr, nc, r, c):
        for row , col in self.dirs:
            cand_row, cand_col = nr + row , nc + col
            if cand_row >= r or cand_row < 0: 
                continue
            if cand_col >= c or cand_col < 0:
                continue
            if self.grid[cand_row][cand_col] == 0:
                continue
            if (cand_row, cand_col) in self.visited:
                continue
            self.visited.add((nr+row, nc + col))
            self.traverse(cand_row, cand_col, r, c)
            self.seen += 1
        

