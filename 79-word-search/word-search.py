class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        board_freq = Counter(ch for row in board for ch in row)
        target_freq = Counter(word)

        for char, freq in target_freq.items():
            if board_freq[char] < freq:
                return False
        
        if board_freq[word[0]] > board_freq[word[-1]]:
            word = word[::-1]

        def dfs(r, c, idx):
            if idx == len(word):
                return True
            if not (0 <= r < rows and 0 <= c < cols):
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
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False
                