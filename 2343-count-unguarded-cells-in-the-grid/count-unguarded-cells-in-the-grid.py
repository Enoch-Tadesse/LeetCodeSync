class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        guards = set((i , j) for i , j in guards)
        walls = set((i, j) for i , j in walls)
        ans = set([(j, i) for i in range(n) for j in range(m) if (j, i) not in walls and (j , i) not in guards])
        vert = set()
        hori = set()
        for r, c in guards:
            nr, nc = r, c + 1
            while (nr, nc) not in walls and (nr, nc) not in guards and (nr, nc) not in hori:
                if nc >= n:
                    break
                hori.add((nr, nc))
                ans.discard((nr, nc))
                nc += 1
            nr, nc = r, c - 1
            while (nr, nc) not in walls and (nr, nc) not in guards and (nr, nc) not in hori:
                if nc < 0:
                    break
                hori.add((nr, nc))
                ans.discard((nr, nc))
                nc -= 1
            nr, nc = r + 1, c
            while (nr, nc) not in walls and (nr, nc) not in guards and (nr, nc) not in vert:
                if nr >= m:
                    break
                vert.add((nr, nc))
                ans.discard((nr, nc))
                nr += 1
            nr, nc = r - 1, c
            while (nr, nc) not in walls and (nr, nc) not in guards and (nr, nc) not in vert:
                if (nr) < 0:
                    break
                vert.add((nr, nc))
                ans.discard((nr, nc))
                nr -= 1
        return len(ans)
