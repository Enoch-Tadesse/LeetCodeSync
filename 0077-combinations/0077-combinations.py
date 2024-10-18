class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res , sol = [] , []

        def backtrack(i,start):
            if i == k:
                res.append(sol[:])
                return
            for j in range(start,n+1):
                sol.append(j)
                backtrack(i+1,j+1)
                sol.pop()
        backtrack(0,1)
        return res