class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])

        def dfs(r, c, idx):
            if idx == len(word):
                return True
            if not (0 <= r < row and 0 <= c < col):
                return False
            if board[r][c] != word[idx]:
                return False
            temp = board[r][c]
            board[r][c] = "#"
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dx, c + dy
                if dfs(nr, nc, idx + 1):
                    # no more search
                    board[r][c] = temp
                    return True
            board[r][c] = temp
            return False
        for r in range(row):
            for c in range(col):
                if dfs(r, c, 0):
                    return True
        return False
                