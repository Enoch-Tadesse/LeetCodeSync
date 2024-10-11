class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        sol = []
        def back(start):
            if len(sol) == k:
                res.append(sol[:])
                return
            for i in range(start,n+1):
                sol.append(i)
                back(i+1)
                sol.pop()
        back(1)
        return res