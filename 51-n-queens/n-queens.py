class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.ldiag = set()
        self.rdiag = set()
        self.col = set()
        self.ans = []
        self.temp = [["."] * n for _ in range(n)]
        self.back( n, 0)
        return self.ans
    def back(self, n, r):
        if r == n:
            res = []
            for r in range(n):
                res.append("".join(self.temp[r]))
            self.ans.append(res)
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
