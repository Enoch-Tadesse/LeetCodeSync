class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        pre = [[0] * (n + 1) for _ in range(n + 1)]

        for r1, c1, r2, c2 in queries:
            pre[r1][c1] += 1
            pre[r2 + 1][c2 + 1] += 1
            pre[r2 + 1][c1] -= 1
            pre[r1][c2 + 1] -= 1
        ans = [[0] * (n) for _ in range(n)]
        for i in range(n):
            for j in range(n):
                add = 0 if i == 0 else ans[i-1][j]
                add2 = 0 if j == 0 else ans[i][j-1]
                minus = 0 if i == 0 or j == 0 else ans[i-1][j-1]
                ans[i][j] = pre[i][j] + add + add2 - minus
        return ans
        
