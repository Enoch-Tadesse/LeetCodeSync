class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows, cols = len(img) , len(img[0])

        ans = [[0] * cols for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                _sum = 0
                _count = 0
                for nr in range(max(0, r - 1), min(r + 2, rows)):
                    for nc in range(max(0, c - 1), min(c + 2, cols)):
                        _sum += img[nr][nc]
                        _count += 1
                ans[r][c] = _sum // _count
        return ans