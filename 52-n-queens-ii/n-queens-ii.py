class Solution:
    def totalNQueens(self, n: int) -> int:
        self.ldiag = set()
        self.rdiag = set()
        self.col = set()
        self.ans = 0
        self.temp = [["."] * n for _ in range(n)]
        self.back( n, 0)
        return self.ans
    def back(self, n, r):
        if r == n:
            self.ans += 1
            return
        for c in range(n):
            if r - c in self.ldiag or r + c in self.rdiag or c in self.col:
                continue
            self.ldiag.add(r - c)
            self.rdiag.add(r + c)
            self.col.add(c)
            self.temp[r][c] = "Q"

            self.back(n , r + 1)

            self.temp[r][c] = "."
            self.col.discard(c)
            self.rdiag.discard(r + c)
            self.ldiag.discard(r - c)
