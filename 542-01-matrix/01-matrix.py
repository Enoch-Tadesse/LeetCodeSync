class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ans = [[-1] * len(mat[0]) for _ in range(len(mat))]
        q = deque([])
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c] == 0:
                    q.append((r, c))
                    ans[r][c] = 0
        depth = -1
        while q:
            depth += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                for nr, nc in [(r-1, c), (r + 1, c) , (r, c+ 1), (r, c-1)]:
                    if (nr < 0 or nc < 0 or nr == len(mat) or nc == len(mat[0])):
                        continue
                    if ans[nr][nc] != -1:
                        continue
                    ans[nr][nc] = depth + 1
                    q.append((nr, nc))
        return ans
            