class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        # E23
        # 2x2
        # 12s
        # [[0, 2, 5], 
        # [2, 0, 7],
        # [3, 5, 7]]
        rows, cols = len(board), len(board[0])
        _max = [[0] * rows for _ in range(cols)]
        _ways = [[0] * rows for _ in range(cols)]
        _ways[0][0] = 1
        dirs = [(0, 1), (1, 0), (1, 1)]
        def valid(x, y):
            return 0 <= x < rows and 0 <= y < cols
        mod = 10 ** 9 + 7
        for r in range(rows):
            for c in range(cols):
                if _max[r][c] == 0 and not (r == 0 and c == 0): continue
                for dr,dc in dirs:
                    nr, nc = dr + r, dc + c
                    if not valid(nr, nc): continue
                    if board[nr][nc] == 'X': continue
                    val = _max[r][c] + int(board[nr][nc] if board[nr][nc] != "S" else 0)
                    if val < _max[nr][nc]:
                        continue
                    if _max[nr][nc] != val:
                        _ways[nr][nc] = 0
                    _max[nr][nc] = val
                    _ways[nr][nc] = (_ways[nr][nc] + _ways[r][c]) % mod
        return [_max[-1][-1], _ways[-1][-1]]