class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = defaultdict(set)
        cols = defaultdict(set)
        comp = defaultdict(set)
        empty = []
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] != ".":
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    comp[(r // 3 , c // 3)].add(board[r][c])
                else:
                    empty.append((r, c))

        def can(r, c, num):
            if num in rows[r] or num in cols[c] or num in comp[(r//3, c//3)]:
                return False
            return True
        def insert(r, c, num):
            rows[r].add(num)
            cols[c].add(num)
            comp[(r//3, c//3)].add(num)
        def remove(r, c, num):
            rows[r].discard(num)
            cols[c].discard(num)
            comp[(r//3, c//3)].discard(num)

        def back(i):
            if i == len(empty):
                return True
            r, c = empty[i]
            for num in map(str, range(1, 10)):
                if not can(r, c, num):
                    continue
                insert(r, c, num)
                board[r][c] = num
                if back(i + 1):
                    return True
                board[r][c] = "."
                remove(r, c, num)
        back(0)