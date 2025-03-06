class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        arr = [0] * (n * n + 1)
        ans = [0, 0]
        for r in range(n):
            for c in range(n):
                arr[grid[r][c]] += 1
                if arr[grid[r][c]] == 2:
                    ans[0] = grid[r][c]
        for i in range(1, n*n + 1):
            if arr[i] == 0:
                ans[1] = i
                break        
        return ans