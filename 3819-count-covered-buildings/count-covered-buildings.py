class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        nums = buildings
        rows = defaultdict(list)
        cols = defaultdict(list)
        counter = 0

        for r , c in nums:
            rows[r].append(c)
            cols[c].append(r)
        for r in rows:
            rows[r].sort()
        for c in cols:
            cols[c].sort()
        for r, c in nums:
            if cols[c][0] < r < cols[c][-1] and rows[r][0] < c < rows[r][-1]:
                counter += 1
        return counter
        