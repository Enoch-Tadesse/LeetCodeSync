class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        freshes = 0
        rottens = deque()
        min = -1
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    freshes += 1
                if grid[r][c] == 2:
                    rottens.append((r,c))
        if freshes == 0:
            return 0
        dir = [(-1,0), (1, 0), (0, -1), (0, 1)]
        while rottens:
            min+=1
            for _ in range(len(rottens)):
                row , col = rottens.popleft()
                for i , j in dir:
                    x , y = i + row, j + col
                    if 0 <= x < len(grid) and 0<= y < len(grid[0]) and grid[x][y] == 1:
                        grid[x][y] = 2
                        freshes-=1
                        rottens.append((x,y))
            

        if freshes > 0:
            return -1
        return min
