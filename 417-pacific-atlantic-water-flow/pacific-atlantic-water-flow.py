class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac = [(0, i) for i in range(cols)] + [(i, 0) for i in range(rows)] 
        atl = [(rows - 1, i) for i in range(cols)] + [(i, cols - 1) for i in range(rows)]
        cand1 = self.tosome(pac, heights)
        cand2 = self.tosome(atl, heights)
        return list(cand1 & cand2)

    def tosome(self, cap, heights):
        q = deque(cap)
        visited = set()
        while q:
            for _ in range(len(q)):
                cr, cc = q.popleft()
                visited.add((cr, cc))

                dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
                for dr, dc in dirs:
                    nr , nc = dr + cr , dc + cc
                    if (nr, nc) in visited:
                        continue
                    if not(0 <= nr < len(heights)) or not(0 <= nc < len(heights[0])):
                        continue
                    if heights[nr][nc] < heights[cr][cc]:
                        continue
                    q.append((nr, nc))
        return visited