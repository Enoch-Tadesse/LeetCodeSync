class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        # m * n * 9

        rows, cols = len(img), len(img[0])

        out = [[0] * cols for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                _count = 0
                _sum = 0
                # process the _count and _sum

                for new_row in range(max(0, r - 1), min(rows, r + 2)):
                    for new_col in range(max(0, c - 1), min(cols, c + 2)):
                        _count += 1
                        _sum += img[new_row][new_col]

                out[r][c] = _sum // _count
        return out