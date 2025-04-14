class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.visited = set()
        for r in range(len(board)):
            for c in range(len(board[0])):
                self.path = set()
                if board[r][c] == "O" and (r,c) not in self.visited:
                    can = self.traverse(r, c, board)
                    if can:
                        for (nr, nc) in self.path:
                            board[nr][nc] = 'X'
        
    def traverse(self, r, c, board):
        stack = [(r, c)]
        can = True
        n = len(board)
        m = len(board[0])
        while stack:
            nr, nc = stack.pop()
            if (nc == 0 or nc == m - 1 or nr == 0 or nr == n - 1):
                can = False
            self.visited.add((nr, nc))
            self.path.add((nr, nc))
            for (nr, nc) in [(nr - 1, nc), (nr + 1, nc), (nr, nc - 1), (nr, nc + 1)]:    
                if (nc < 0 or nr < 0 or nc >= m or nr >= n):
                    continue
                if (nr, nc) not in self.visited and board[nr][nc] == "O":
                    stack.append((nr, nc))
        return can

