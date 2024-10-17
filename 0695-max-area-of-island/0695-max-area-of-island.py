class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0
        visited = set()
        dir = [(-1,0), (0, -1), (1, 0), (0, 1)]
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and grid[r][c] not in visited:
                    area = max(area, self.explore(grid, r, c, visited, dir))
        return area
    def explore(self, grid, r, c, visited, dir):
        if grid[r][c] == 0:
            return 0
        size = 1
        visited.add((r,c))
        for i , j in dir:
            x , y = i + r, j + c
            if (0 <= x < len(grid) and 0<= y < len(grid[0])) and grid[x][y] == 1 and (x,y) not in visited:
                # visited.add((x,y))
                size+=self.explore(grid, x, y, visited, dir)
        return size
        